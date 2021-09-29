from django.db import models
from django.http import request


TREATMENT_CHOICES = (
    ('Tartar removal: 50€','TARTAR REMOVAL: 50€'),
    ('Teeth whitening: 250€', 'TEETH WHITENING: 250€'),
    ('Tooth removal: 150€','TOOTH REMOVAL: 150€'),
    ('Braces: 2400€','BRACES: 2400€'),
)


class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    treatment = models.CharField(max_length=30, choices=TREATMENT_CHOICES, default='Tartar removal: 50€')
    datetime = models.DateField(auto_now_add=False, null=True, blank=True)
    information = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]
