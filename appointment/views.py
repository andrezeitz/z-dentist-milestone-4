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


class PriceTemplateView(TemplateView):
    """
    A view that renders the price template
    """
    template_name = 'price.html'


class ManageAppointmentTemplateView(ListView):
    """
    A view that renders a template and read the information from the database.
    The appointment information will be shown in cards and the admin will be
    able to accept the appointment
    """
    template_name = 'manage_appointments.html'
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 6

    
