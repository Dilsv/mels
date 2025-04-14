from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from django.shortcuts import get_object_or_404


def services(request):
    return render(request, 'services.html')


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            # Save the form data to the database
            form.save()
            # Display a success message and redirect to the booking list
            return render(
                request,
                'services/bookings_list.html',
                {
                    'bookings': Booking.objects.filter(user=request.user),
                    'message': 'Booking request submitted successfully!'
                }
            )
        else:
            # If the form is not valid, render the page with errors
            return render(request, 'booking_create.html', {'form': form})
    else:
        form = BookingForm()

    return render(request, 'booking_create.html', {'form': form})


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(
        request, 'services/bookings_list.html',
        {'bookings': bookings}
    )


@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return render(
                request,
                'services/bookings_list.html',
                {
                    'bookings': Booking.objects.filter(user=request.user),
                    'message': 'Booking request updated successfully!'
                }
            )
    else:
        form = BookingForm(instance=booking)

    return render(
        request, 'services/booking_edit.html',
        {'form': form, 'booking': booking}
    )


@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(
        request, 'services/booking_delete.html',
        {'booking': booking}
    )
