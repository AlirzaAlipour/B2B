from threading import Thread
from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.test import APIClient
from merchants.models import MerchantAPIKey
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class ThreadedTopUpTest(TransactionTestCase):  # Inherit from TransactionTestCase
    def setUp(self):
        # Create merchant with sufficient balance
        self.user = User.objects.create_user(email='merchantt@test.com', password='pass', username='username')
        self.merchant = self.user.merchant
        self.merchant.balance = 10000
        self.merchant.save()
        # Create API key (assuming create_key returns (instance, key_str))
        _, self.api_key = MerchantAPIKey.objects.create_key(merchant=self.merchant, name='name')
        self.url = reverse('topup')
        self.total_amount = 0

    def _send_batch(self):

        for _ in range(500):
            # Create a new client for each request to avoid thread issues
            client = APIClient()
            client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key}')
            amount = random.randint(1, 10)  
            phone_number = f'123456789{_}'  
            data = {
                'amount': amount,
                'phone_number': phone_number,
            }
            response = client.post(self.url, data)
            self.assertEqual(response.status_code, 201)  # Ensure request is successful
            self.total_amount += amount


    def test_2_thread_500_requests(self):

        threads = [Thread(target=self._send_batch) for _ in range(2)]
        
        for t in threads:
            t.start()
            
        for t in threads:
            t.join()

        self.merchant.refresh_from_db()
        self.assertEqual(self.merchant.balance , 10000 - self.total_amount)
        self.assertEqual(self.merchant.topup_requests.count(), 1000)