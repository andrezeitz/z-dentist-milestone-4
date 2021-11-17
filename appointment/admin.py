from django.contrib import admin
from .models import Appointment


# This class define which department columns will be shown in Admin site
class AppointmentAdmin(admin.ModelAdmin):
    # A list of displayed columns name.
    list_display = ['id', 'first_name', 'last_name', 'email']

    # Define search columns list, then a search box will be added at the top
    search_fields = ['id', 'first_name', 'last_name', 'email']


admin.site.register(Appointment, AppointmentAdmin)
