from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from pyparsing import identchars
from hotel_app.froms import HabitacionForm
from hotel_app.models import Habitacion, Hotel


@permission_required('hotel_app.view_habitacion')
def habitacion_admin_inicio(request, idh):
    hotel = get_object_or_404(Hotel, id=idh)
    habitaciones = Habitacion.objects.filter(hotel=idh).order_by('numero')
    pagina = request.GET.get('page', 1)
    try:
        paginator = Paginator(habitaciones, 10)
        habitaciones = paginator.page(pagina)
    except:
        raise Http404
    data = {
        'lista': habitaciones,
        'hotel': hotel,
        'paginator': paginator
    }
    return render(request, 'administrador/habitacion/inicio.html', data)


@permission_required('hotel_app.add_habitacion')
def habitacion_admin_agregar(request, idh):
    hotel = get_object_or_404(Hotel, id=idh)
    data = {'form': HabitacionForm, 'hotel': hotel}
    if request.method == 'POST':
        form = HabitacionForm(data=request.POST, files=request.FILES)
        existe = Habitacion.objects.filter(
            numero=form.data['numero'], hotel=hotel.id)
        if len(existe) > 0:
            messages.warning(request, "La habitacion ya existe.")
            return redirect(to="habitacion_admin_inicio", idh=hotel.id)
        else:
            if form.is_valid():
                habitacion = Habitacion()
                habitacion.numero = form.cleaned_data['numero']
                habitacion.tipo = form.cleaned_data['tipo']
                habitacion.cama = form.cleaned_data['cama']
                habitacion.hospedaje = form.cleaned_data['hospedaje']
                habitacion.valor = form.cleaned_data['valor']
                habitacion.imagen = form.cleaned_data['imagen']
                habitacion.descripcion = form.cleaned_data['descripcion']
                habitacion.hotel = hotel
                habitacion.save()
                messages.success(request, 'Habitacion creada.')
                return redirect(to='habitacion_admin_inicio', idh=hotel.id)
            else:
                data['form'] = form
    return render(request, 'administrador/habitacion/agregar.html', data)


@permission_required('hotel_app.delete_habitacion')
def habitacion_admin_eliminar(request, idh, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    habitacion.delete()
    messages.success(request, "Habitacion eliminada.")
    return redirect(to='habitacion_admin_inicio', idh=idh)


@permission_required('hotel_app.change_habitacion')
def habitacion_admin_modificar(request, idh, id):
    hotel = get_object_or_404(Hotel, id=idh)
    habitacion = get_object_or_404(Habitacion, id=id)
    data = {'form': HabitacionForm(instance=habitacion), 'hotel': hotel}
    if request.method == 'POST':
        form = HabitacionForm(
            data=request.POST, instance=habitacion, files=request.FILES)
        if form.is_valid():
            n_habitacion = Habitacion()
            n_habitacion.id = id
            n_habitacion.numero = habitacion.numero
            n_habitacion.tipo = form.cleaned_data['tipo']
            n_habitacion.cama = form.cleaned_data['cama']
            n_habitacion.hospedaje = form.cleaned_data['hospedaje']
            n_habitacion.valor = form.cleaned_data['valor']
            n_habitacion.imagen = form.cleaned_data['imagen']
            n_habitacion.descripcion = form.cleaned_data['descripcion']
            n_habitacion.hotel = hotel
            n_habitacion.save()
            messages.success(request, 'Habitacion modificada.')
            return redirect(to='habitacion_admin_inicio', idh=hotel.id)
        else:
            data['form'] = form
    return render(request, 'administrador/habitacion/modificar.html', data)
