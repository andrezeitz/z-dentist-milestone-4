from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from emailer import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin:login'),
    path('', include('appointment.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path("services/", TemplateView.as_view(template_name='services.html'),
         name="services"),
    path('contact-us/', TemplateView.as_view(template_name='contact_us.html'),
         name='contact_us'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
    path('accounts/', include('allauth.urls')),
]
