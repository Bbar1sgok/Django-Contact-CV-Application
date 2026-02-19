from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


# Contact Form
# Handles user input validation and email sending logic

class ContactForm(forms.Form):

    # Sender's name
    name = forms.CharField(
        max_length=100,
        required=True,
    )

    # Sender's email address (validated as proper email format)
    email = forms.EmailField(
        max_length=254,
        required=True,
    )

    # Message subject
    subject = forms.CharField(
        max_length=254,
        required=True,
    )

    # Message body (rendered as textarea in template)
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

   
    # Sends email after form validation
   
    def send_mail(self):

        # Ensure form is valid before sending email
        if not self.is_valid():
            return False

        # Retrieve validated data
        name = self.cleaned_data['name']
        sender_email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        # Build email body content
        message_context = (
            f"Message received.\n\n"
            f"Name: {name}\n"
            f"Subject: {subject}\n"
            f"Email: {sender_email}\n"
            f"Message: {message}"
        )

        # Create email instance using Django EmailMessage
        email_message = EmailMessage(
            subject=subject,
            body=message_context,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[sender_email],  # Allows direct reply to sender
        )

        # Send email (raises error if fails)
        email_message.send(fail_silently=False)

        return True