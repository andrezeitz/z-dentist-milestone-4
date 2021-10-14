from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Appointment
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.conf import settings



class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class AppointmentTemplateView(TemplateView):
    template_name = 'appointment.html'

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        treatment = request.POST.get('treatment')
        datetime = request.POST.get('datetime')
        information = request.POST.get('information')

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            treatment=treatment,
            datetime=datetime,
            information=information
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f'Thanks {fname} for the booking.')
        return HttpResponseRedirect(request.path)


class ContactUsTemplateView(TemplateView):
    template_name = 'contact_us.html'

    def post(self, request):
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')

        email = EmailMessage(
            subject=f"{name} from Dentist Z.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponseRedirect(request.path)


class PriceTemplateView(TemplateView):
    template_name = 'price.html'
