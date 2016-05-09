from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse

from papierbackup import settings
from .models import Document, Category


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

class DocumentViewTests(TestCase):

    def test_document_list_without_auth_redirect_to_login(self):
        document_list_url = reverse('document-list')
        response = self.client.get(document_list_url)
        self.assertEqual(response.status_code, 302)
        expected_url = '{}?next={}'.format(settings.LOGIN_URL, document_list_url)
        self.assertEqual(response.url, expected_url)

    def test_document_detail_without_auth_redirect_to_login(self):
        document_detail_url = reverse('document-detail', args=[42])
        response = self.client.get(document_detail_url)
        self.assertEqual(response.status_code, 302)
        expected_url = '{}?next={}'.format(settings.LOGIN_URL, document_detail_url)
        self.assertEqual(response.url, expected_url)

    def test_document_detail_non_readable_by_non_owner(self):
        """Ensure it's not possible for an user to access document owned by other users."""
        # Create two users
        user_bob = User.objects.create_user('bob')
        user_bob.save()
        user_roger = User.objects.create_user('roger')
        user_roger.save()
        # Create document owned by bob
        cat = Category(name='Passeport')
        cat.save()
        doc = Document(user=user_bob, category=cat)
        doc.save()
        # Roger must not be able to read it
        self.client.force_login(user_roger)
        res = self.client.get(reverse('document-detail', args=[doc.pk]))
        self.assertEqual(res.status_code, 404)
