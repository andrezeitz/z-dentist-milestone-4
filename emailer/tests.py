from django.test import TestCase
from django.core import mail


class EmailTest(TestCase):
    """
    Testing send_mail
    """
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
