from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from hotel_app.froms import HotelForm
from hotel_app.models import Hotel


@permission_required('hotel_app.view_hotel')
def hotel_admin_inicio(request):
    hoteles = Hotel.objects.all().order_by('nombre')
    pagina = request.GET.get('page', 1)
    pl = int(pagina)-5
    print(f'Tipo &{type(pl)} ${pl}')
    try:
        paginator = Paginator(hoteles, 12)
        hoteles = paginator.page(pagina)
    except:
        raise Http404
    data = {
        'lista': hoteles,
        'paginator': paginator,
        'pl': pl
    }
    return render(request, 'administrador/hotel/inicio.html', data)


@permission_required('hotel_app.add_hotel')
def hotel_admin_agregar(request):
    data = {'form': HotelForm}
    if request.method == 'POST':
        form = HotelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel creado.')
            return redirect(to='hotel_admin_inicio')
        else:
            data['form'] = form
    return render(request, 'administrador/hotel/agregar.html', data)


@permission_required('hotel_app.delete_hotel')
def hotel_admin_eliminar(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    hotel.delete()
    messages.success(request, "Hotel eliminado.")
    return redirect(to='hotel_admin_inicio')


@permission_required('hotel_app.change_hotel')
def hotel_admin_modificar(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    data = {'hotel': hotel, 'form': HotelForm(instance=hotel)}
    if request.method == 'POST':
        form = HotelForm(data=request.POST, instance=hotel,
                         files=request.FILES)
        if form.is_valid():
            hotel = Hotel()
            hotel.id = id
            hotel.nombre = form.cleaned_data['nombre']
            hotel.ciudad = form.cleaned_data['ciudad']
            hotel.direccion = form.cleaned_data['direccion']
            hotel.descripcion = form.cleaned_data['descripcion']
            hotel.logo = form.cleaned_data['logo']
            hotel.imagen = form.cleaned_data['imagen']
            hotel.save()
            messages.success(request, 'Hotel modificado.')
            return redirect(to='hotel_admin_inicio')
        else:
            data['form'] = form
    return render(request, 'administrador/hotel/modificar.html', data)
