from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('request')


