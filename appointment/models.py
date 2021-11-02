from django.db import models
from django.http import request


TREATMENT_CHOICES = (
    ('Basic dentist Survey: 100€', 'BASIC DENTIST SURVEY: 100€'),
    ('Teeth whitening Service: 300€', 'TEETH WHITENING SERVICE: 300€'),
    ('Ceramic crowns and fillings: 100€', 'CERAMIC CROWNS AND FILLINGS: 100€'),
    ('Remove crowns, bridges Service: 50€', 'REMOVE CROWNS, BRIDGES SERVICE: 50€'),
    ('Overlay teeth whitening: 170€', 'OVERLAY TEETH WHITENING: 170€'),
    ('Make Braces: 2400€', 'MAKE BRACES: 2400€'),
    ('Covering the recession of the gums: 400€', 'COVERING THE RECESSION OF THE GUMS: 400€'),
    ('Removal of tooth: 150€', 'REMOVAL OF TOOTH: 150€'),
    ('Removal of tartar: 50€', 'REMOVAL OF TARTAR: 50€'),
)


class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES, default='Basic dentist survey: 100€')
    datetime = models.DateField(auto_now_add=False, null=True, blank=True)
    information = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=False, null=True, auto_now_add=False,)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]
