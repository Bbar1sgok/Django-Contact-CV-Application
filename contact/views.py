from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
from contact.forms import ContactForm


# Contact form submission endpoint (AJAX-based)
# Handles POST requests and returns JSON response

def contact_form(request):

    # Allow only POST requests
    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Invalid request method"
        }, status=400)

    # Bind submitted form data
    form = ContactForm(request.POST)

    # Validate form data
    if not form.is_valid():
        return JsonResponse({
            "success": False,
            "message": "Form is not valid"
        }, status=400)

    # Save validated message to database
    Message.objects.create(
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        subject=form.cleaned_data['subject'],
        message=form.cleaned_data['message'],
    )

    # Trigger email sending logic defined inside the form
    form.send_mail()

    # Return success response
    return JsonResponse({
        "success": True,
        "message": "Contact form sent successfully"
    })



# Contact page view
# Renders contact template with empty form instance

def contact(request):

    # Initialize empty contact form
    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact.html', context)