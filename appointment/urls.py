from django.urls import path
from .views import AppointmentTemplateView, ManageAppointmentTemplateView
from . import views


urlpatterns = [
    path("make-an-appointment/", AppointmentTemplateView.as_view(),
         name="appointment"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(),
         name="manage_appointments"),
    path('delete_appointment/<appointment_id>', views.delete_appointment,
         name='delete-appointment'),
]
