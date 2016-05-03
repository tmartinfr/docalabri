from datetime import datetime, timedelta

from django.test import TestCase

from .models import Document

# Create your tests here.

class DocumentTests(TestCase):

    def test_document_expire_soon_with_soon_date(self):
        # expire_soon() should return True if document expires in less than 30 days.
        soon_date = datetime.now().date() + timedelta(29)
        document = Document(expiration_date=soon_date)
        self.assertEqual(document.expire_soon(), True)

    def test_document_expire_soon_with_far_date(self):
        # expire_soon() should return False if document expires in more than 30 days.
        far_date = datetime.now().date() + timedelta(31)
        document = Document(expiration_date=far_date)
        self.assertEqual(document.expire_soon(), False)