from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Appointment
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages


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