# services/forms.py

from django import forms

class BookingForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    service = forms.ChoiceField(
        label='Service',
        choices=[
            ('natural', 'Natural'),
            ('glam', 'Glam'),
            ('bridal', 'Bridal'),
            ('hd', 'HD')
        ]
    )
    preferred_date = forms.DateField(label='Preferred Date', widget=forms.TextInput(attrs={'type': 'date'}))
    message = forms.CharField(label='Additional Information', widget=forms.Textarea, required=False)
