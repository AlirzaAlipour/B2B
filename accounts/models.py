from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(AbstractUser):
    """
    Using Multiple Models: Type Safety, Clear Separation, Authentication Complexity
    Single user model with role differentiation: Simpler Authentication, Less Type Safety, Complex Validation: ensure profile data matches user type
    """
    USER_TYPES = [
        ('ADMIN', 'Administrator'),
        ('SALESMAN', 'Salesman'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)


class AdminProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_profile')
    department = models.CharField(max_length=100)


class SalesmanProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='salesman_profile')
    company_name = models.CharField(max_length=100)
    current_balance = models.PositiveIntegerField(default=0)