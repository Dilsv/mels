from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def services(request):
    return render(request, 'services.html')

def booking(request):
    return render(request, 'booking.html')
