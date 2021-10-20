from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.conf import settings
from django.views.generic import ListView
from .models import Appointment


class HomeTemplateView(TemplateView):
    """
    A view that renders the index template
    """
    template_name = 'index.html'


class AppointmentTemplateView(TemplateView):
    """
    A view that renders a template and also save all appointment information
    to the database.
    It will also show a success message to the user after complete the form
    """
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

        messages.add_message(request, messages.SUCCESS, f'Thank you {fname} for the booking. We will confirm you appointment as soon as possible. ')
        return HttpResponseRedirect(request.path)


class TemplateEmail(View):
    """
    A view that renders a template and also let the customer email the company
    """
    # template_name = 'contact_us.html'

    # def post(self, request):
    #     name = request.POST.get('message-name')
    #     email = request.POST.get('message-email')
    #     message = request.POST.get('message')

    #     email = EmailMessage(
    #         subject=f"{name} from Dentist Z.",
    #         body=message,
    #         from_email=settings.EMAIL_HOST_USER,
    #         to=[settings.EMAIL_HOST_USER],
    #         reply_to=[email]
    #     )
    #     email.send()
    #     return HttpResponseRedirect(request.path)


class PriceTemplateView(TemplateView):
    """
    A view that renders the price template
    """
    template_name = 'price.html'


class ManageAppointmentTemplateView(TemplateView):
    """
    A view that renders a template and read the information from the database.
    The appointment information will be shown in cards and the admin will be
    able to accept the appointment
    """
    template_name = 'manage_appointments.html'
    model = Appointment
    login_required = True
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "appointments": appointments
        })
        return context


