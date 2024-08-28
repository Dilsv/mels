from django import forms
from .models import Booking  # Import the Booking model

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'date', 'time', 'message']  # Specify the fields to be included in the form
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'service': 'Service',
            'date': 'Preferred Date',
            'time': 'Preferred Time',
            'message': 'Additional Information',
        }
