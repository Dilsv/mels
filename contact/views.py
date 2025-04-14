from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.utils.html import strip_tags


def contact(request):
    """ A view to return the contact page with
    the contact form.
    Save the contact form data to the database
    and send an email to the admin.
    """
    # get the contact form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # strip the html tags from the message
            message = form.cleaned_data['message']
            message = strip_tags(message)
            message = message.replace("&nbsp;", " ")
            message = str(message).strip()

            # check if the form is empty
            if message == '':
                messages.error(request, "You can't submit an empty form")
            else:
                form.save()
                messages.success(request, 'Form submitted successfully')
                return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})