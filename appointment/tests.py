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









# class TestGroupAdmin(TestCase):

#     def setUp(self):
#         self.client = Client()
#         User.objects.create_superuser(
#             username='superuser', password='secret', email='admin@example.com'
#         )
#         c.force_login(username='superuser', password='secret')

#     def test_manage_appointment(self):
#         # run test
#         response = self.client.get('/manage-appointments/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "manage_appointments.html")


    # def test_manage_appointment(self, request):
    #     # if user not logged in try to enter page should redirect to login
    #         response = self.client.get('/manage-appointments')
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, "manage-appointments.html")


    #     else:
    #         response = self.client.get('/manage-appointments')
    #         self.assertEqual(response.status_code, 302)
    #         self.assertTemplateUsed(response, "manage-appointments.html")







# class MakeAppoinmentTestCase(TestCase):

#     def test_appointment_form(self):
#         form_data = {'first_name': 'andre',
#                      'last_name': 'zeitz',
#                      'email': 'andre@email.com',
#                      'phone': '09239238',
#                      'treatment': 'Basic dentist survey: 100€',
#                      'datetime': '24-11-2021',
#                      'information': 'fast please'}
#         form = form-card
#         self.assertTrue(form.is_valid())



