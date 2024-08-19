# services/views.py

from django.shortcuts import render
from .forms import BookingForm

def services(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # For example, save to database or send an email
            # form.save()
            # send_email(form.cleaned_data)
            return render(request, 'services.html', {'form': form, 'message': 'Booking request submitted successfully!'})
    
    return render(request, 'services.html', {'form': form})
