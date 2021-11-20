from django.test import TestCase, Client
from .models import Appointment
from django.contrib.auth.models import User, Group
from django.urls import reverse


# Create your tests here.


class MainPagesTestCase(TestCase):
    """
    Testing load of all main pagaes
    """
    def test_indexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_services(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services.html")
        self.assertTemplateUsed(response, "base.html")

    def test_make_appointment(self):
        response = self.client.get('/make-an-appointment/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment.html')
        self.assertTemplateUsed(response, "base.html")

    def test_contact(self):
        response = self.client.get('/contact-us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_us.html")
        self.assertTemplateUsed(response, "base.html")


class UserTests(TestCase):
    """
    Testing load of login and signup pages and if user try to enter
    logout page when not logged in it will redicrect to index page
    """
    def test_register_page_load(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_load(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
    
    # if user try to enter page not logged in will be redicrect to index page
    def test_logout_page_load(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)


