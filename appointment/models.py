from django.db import models
from django.contrib.auth.models import User


TREATMENT_CHOICES = (
    ('Basic dentist Survey: 100€', 'BASIC DENTIST SURVEY: 100€'),
    ('Teeth whitening Service: 300€', 'TEETH WHITENING SERVICE: 300€'),
    ('Ceramic crowns and fillings: 100€', 'CERAMIC CROWNS AND FILLINGS: 100€'),
    ('Remove crowns, bridges Service: 50€',
     'REMOVE CROWNS, BRIDGES SERVICE: 50€'),
    ('Overlay teeth whitening: 170€', 'OVERLAY TEETH WHITENING: 170€'),
    ('Make Braces: 2400€', 'MAKE BRACES: 2400€'),
    ('Covering the recession of the gums: 400€',
     'COVERING THE RECESSION OF THE GUMS: 400€'),
    ('Removal of tooth: 150€', 'REMOVAL OF TOOTH: 150€'),
    ('Removal of tartar: 50€', 'REMOVAL OF TARTAR: 50€'),
)


class Appointment(models.Model):
    """
    Models for appointments and user to be able to use foreign key
    """
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(max_length=50, unique=False)
    phone = models.CharField(max_length=50, unique=False)
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES,
                                 default='Basic dentist survey: 100€')
    datetime = models.DateField(auto_now_add=False, null=True, blank=True)
    information = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=False, null=True,
                                         auto_now_add=False,)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)

    # Define string representation for this model class,
    # It will be used when display model class data in Django Admin web site.
    def __str__(self):
        ret = self.first_name + ',' + self.last_name + ',' + self.email
        return ret
