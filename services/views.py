# services/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def services(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = user
            # Save the form data to the database
            form.save()
            # Display a success message and redirect to the same page
            return render(request, 'services.html', {'form': BookingForm(), 'message': 'Booking request submitted successfully!'})
        else:
            # If the form is not valid, render the page with errors
            return render(request, 'services.html', {'form': form})
    else:
        form = BookingForm()

    return render(request, 'services.html', {'form': form})


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'services/booking_list.html', {'bookings': bookings})

@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'services/booking_edit.html', {'form': form, 'booking': booking})

@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'services/booking_delete.html', {'booking': booking})
