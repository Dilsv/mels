from django import forms

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
    # Add date and time fields
    preferred_date = forms.DateField(
        label='Preferred Date', 
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    preferred_time = forms.TimeField(
        label='Preferred Time', 
        widget=forms.TextInput(attrs={'type': 'time'})
    )
    # Add a message field
    message = forms.CharField(
        label='Additional Information', 
        widget=forms.Textarea(attrs={'rows': 4}), 
        required=False
    )
