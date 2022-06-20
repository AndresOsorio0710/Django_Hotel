from django.shortcuts import render


def hotel_inicio(request):
    return render(request, 'hotel/inicio.html')
