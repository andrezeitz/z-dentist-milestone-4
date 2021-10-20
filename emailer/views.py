from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail


class SendFormEmail(View):

    def get(self, request):

        # Get the form data 
        name = request.GET.get('message-name', None)
        email = request.GET.get('message-email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Z Dentist Customer Service',
            'Hello ' + name + ',\n' + message,
            'swe_zeitz@hotmail.com',
            [
                email,
            ]
        )

        # Redirect to same page after form submit
        messages.add_message(request, messages.SUCCESS, f'Thank you {name} for your email. We will answer you as soon as possible. ')
        return redirect('contact_us')
        