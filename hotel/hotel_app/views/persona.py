from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from hotel_app.froms import PersonaForm
from hotel_app.models import Persona


@permission_required('hotel_app.view_persona')
def persona_admin_inicio(request):
    personas = Persona.objects.all().order_by('apellido', 'nombre')
    pagina = request.GET.get('page', 1)
    try:
        paginator = Paginator(personas, 10)
        personas = paginator.page(pagina)
    except:
        raise Http404
    data = {
        'lista': personas,
        'paginator': paginator
    }
    return render(request, 'administrador/persona/inicio.html', data)


@permission_required('hotel_app.add_persona')
def persona_admin_agregar(request):
    data = {'form': PersonaForm}
    if request.method == 'POST':
        form = PersonaForm(data=request.POST)
        try:
            existe = Persona.objects.get(rut=form.data['rut'])
            messages.warning(request, "La persona ya existe.")
            return redirect(to="persona_admin_modificar", id=existe.id)
        except:
            if form.is_valid():
                persona = Persona()
                persona.rut = form.cleaned_data["rut"]
                persona.nombre = form.cleaned_data["nombre"].upper()
                persona.apellido = form.cleaned_data["apellido"].upper()
                persona.pais = form.cleaned_data["pais"].upper()
                persona.telefono = form.cleaned_data["telefono"]
                persona.correo = form.cleaned_data["correo"]
                persona.direccion = form.cleaned_data["direccion"].upper()
                persona.save()
                messages.success(request, "Persona registrada.")
                user = User()
                user.username = persona.rut
                user.first_name = persona.nombre.upper()
                user.last_name = persona.apellido.upper()
                user.email = persona.correo
                user.set_password(persona.rut)
                user.save()
                messages.success(request, "Usuario creado.")
                return redirect(to='persona_admin_inicio')
            else:
                data["form"] = form
    return render(request, 'administrador/persona/agregar.html', data)


@permission_required('hotel_app.delete_persona')
def persona_admin_eliminar(request, id):
    persona = get_object_or_404(Persona, id=id)
    user = get_object_or_404(User, username=persona.rut)
    user.delete()
    persona.delete()
    messages.success(request, "Persona eliminada.")
    return redirect(to='persona_admin_inicio')


@permission_required('hotel_app.change_persona')
def persona_admin_modificar(request, id):
    persona = get_object_or_404(Persona, id=id)
    rut = persona.rut
    correo = persona.correo
    data = {
        'persona': persona,
        'form': PersonaForm(instance=persona)
    }
    if request.method == 'POST':
        form = PersonaForm(data=request.POST, instance=persona)
        if form.is_valid():
            print(rut)
            n_persona = Persona()
            n_persona.id = id
            n_persona.rut = rut
            n_persona.correo = correo
            n_persona.nombre = form.cleaned_data["nombre"].upper()
            n_persona.apellido = form.cleaned_data["apellido"].upper()
            n_persona.pais = form.cleaned_data["pais"].upper()
            n_persona.direccion = form.cleaned_data["direccion"].upper()
            n_persona.telefono = form.cleaned_data["telefono"]
            n_persona.save()
            messages.success(request, "Persona modificada.")
            return redirect(to='persona_admin_inicio')
        else:
            data['form'] = form
    return render(request, 'administrador/persona/modificar.html', data)
