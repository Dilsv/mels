# services/forms.py

from django import forms

from .models import Booking

class BookingForm(forms.Form):
        name = forms.CharField(label='Full Name', max_length=100)
        email = forms.EmailField(label='Email Address')
        phone = forms.CharField(label='Phone Number', max_length=15)
        service = forms.ChoiceField(
            label='Service',
            choices=[
                ('natural', 'Natural'),
                ('glam', 'Glam'),
                ('bridal', 'Bridal'),
                ('hd', 'HD')
            ]
        )