from django.urls import path
from .views import AppointmentTemplateView, ManageAppointmentTemplateView


urlpatterns = [
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(), name="manage_appointments"),
]