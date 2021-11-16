from django.http.response import HttpResponseRedirect
# from django.views.generic import View
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic import ListView
from django.core.mail import send_mail
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Appointment


class AppointmentTemplateView(TemplateView):
    """
    A view that renders a template and also save all appointment information
    to the database.
    It will also show a success message to the user after complete the form
    """
    template_name = 'appointment.html'

    def post(self, request):
        """
        Function that let the form post the details to the backend.
        It also create the models.
        """
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        treatment = request.POST.get('treatment')
        date_time = request.POST.get('datetime')
        information = request.POST.get('information')

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            treatment=treatment,
            datetime=date_time,
            information=information,
            user=request.user,
        )

        appointment.save()

        messages.add_message(
            request, messages.SUCCESS, f"Thank you {fname} for the booking."
            " We will confirm your appointment as soon as possible.")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    """
    A view that renders a template and read the information from the database.
    The appointment information will be shown in cards and the admin will be
    able to accept the appointment. Pagination of 6 cards per each side.
    After accepting the appointment the customer will get a confirmation email.
    """
    template_name = 'manage_appointments.html'

    # Protect page to only logged in users
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Appointment
    context_object_name = "appointments"
    paginate_by = 6

    # Show appointment for only the user
    def get_queryset(self):
        """
        Function that make the user only see there bookings.
        """
        if self.request.user.is_superuser:
            return Appointment.objects.all()
        else:
            return Appointment.objects.filter(user=self.request.user)

    def post(self, request):
        """
        Function that save the confirmed date and appointment-id.
        It also send out a confirmation email to the user and admin.
        """
        accepted_date = request.POST.get('confirm-date', None)
        appointment_id = request.POST.get('appointment-id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.edited = True
        appointment.accepted_date = accepted_date
        appointment.save()

        # Split up the accepted_date to look better
        date = accepted_date[0:10]
        time = accepted_date[11:]

        subject = 'Z Dentist Customer Service'
        body = (
            f"Hello {appointment.first_name}, " +
            f"your booking is confirmed on {date} {time}"
        )
        # Send Confirmation Mail to user and CC to admin
        send_mail(
            subject,
            body,
            'swe_zeitz@hotmail.com',
            [appointment.email, 'swe_zeitz@hotmail.com']
        )

        messages.add_message(
            request, messages.SUCCESS, f"Appointment accepted {date} {time}" +
            f" for {appointment.first_name} {appointment.last_name}.")
        return HttpResponseRedirect(request.path)


def delete_appointment(request, appointment_id):
    """
    Function that let you delete an appointment. After deletion is made a
    confirmation email is send to the user and admin.
    """
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()

    subject = 'Z Dentist Customer Service'
    body = (
        f"Hello {appointment.first_name}, "
        "your booking is now canceled."
    )
    # Send Confirmation Mail to user and CC to admin
    send_mail(
        subject,
        body,
        'swe_zeitz@hotmail.com',
        [appointment.email, 'swe_zeitz@hotmail.com']
    )

    messages.add_message(
        request, messages.SUCCESS, "Booking was deleted from the database.")
    return redirect(reverse('manage_appointments'))
