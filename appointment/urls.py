from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import AppointmentTemplateView, ManageAppointmentTemplateView
from . import views


urlpatterns = [
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(), name="manage_appointments"),
    path('delete_appointment/<appointment_id>', views.delete_appointment, name='delete-appointment'),
    # path('update_appointment/<appointment_id>', views.update_appointment, name='update-appointment'),
]