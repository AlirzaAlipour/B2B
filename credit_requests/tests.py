from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from merchants.models import Merchant
from .models import IncreaseCreditRequest

User = get_user_model()

class CreditRequestDetailViewTest(APITestCase):
    def setUp(self):
        # Create an admin user
        self.admin = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
        # Create a merchant user and ensure it is not already linked to a Merchant
        self.merchant_user = User.objects.create_user(username='merchant', email='merchant@example.com', password='password')
        # Check if the user is already associated with a Merchant
        if not hasattr(self.merchant_user, 'merchant'):
            self.merchant = Merchant.objects.create(user=self.merchant_user, company_name='Test Co', balance=0)
        else:
            self.merchant = self.merchant_user.merchant
        
        # Create a credit request for the merchant
        self.credit_request = IncreaseCreditRequest.objects.create(merchant=self.merchant, amount=100, status='pending')
        # Authenticate the admin user for the client
        self.client.force_authenticate(user=self.admin)
        # Set the URL for the credit request detail view
        self.url = reverse('credit-requests', args=[self.credit_request.id])

    def test_approve_credit_request_increases_balance(self):
        data = {'status': 'approved'}
        response = self.client.patch(self.url, data)
        self.merchant.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.merchant.balance, 100)
        self.credit_request.refresh_from_db()
        self.assertEqual(self.credit_request.status, 'approved')

    def test_reject_credit_request_no_balance_change(self):
        data = {'status': 'rejected'}
        response = self.client.patch(self.url, data)
        self.merchant.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.merchant.balance, 0)
        self.credit_request.refresh_from_db()
        self.assertEqual(self.credit_request.status, 'rejected')