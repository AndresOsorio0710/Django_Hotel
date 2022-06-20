from django.shortcuts import render
from hotel_app.froms import CustomUserCreationForm


def registrar_usuario(request):
    data={
        'form': CustomUserCreationForm()
    }
    return render(request, 'registration/registrar_usuario.html', data)