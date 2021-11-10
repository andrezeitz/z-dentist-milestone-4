from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail


class SendFormEmail(View):
    """
    View that let the user send an email in the contact us form.
    """
    def get(self, request):
        """
        Function that get the form data and send out an email to user and admin
        """
        # Get the form data
        name = request.GET.get('message-name', None)
        email = request.GET.get('message-email', None)
        message = request.GET.get('message', None)

        # Send Email to user and admin
        send_mail(
            'Z Dentist Customer Service',
            'Hello ' + name + ', this was your message to us' ',\n' + message,
            'swe_zeitz@hotmail.com',
            [
                email, 'swe_zeitz@hotmail.com'
            ]
        )

        # Redirect to same page after form submit
        messages.add_message(
            request, messages.SUCCESS, f"Thank you {name} for your email."
            " We will answer you as soon as possible. ")
        return redirect('contact_us')
