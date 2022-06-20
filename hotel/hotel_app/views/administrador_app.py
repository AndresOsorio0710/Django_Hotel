from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('hotel_app.view_user')
def administrador_inicio(request):
    return render(request, 'administrador/inicio.html')