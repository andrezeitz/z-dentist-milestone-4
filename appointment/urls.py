from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ContactUsTemplateView, PriceTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("contact-us/", ContactUsTemplateView.as_view(), name="contact_us"),
    path("pricing/", PriceTemplateView.as_view(), name="price"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(), name="manage_appointments"),
]