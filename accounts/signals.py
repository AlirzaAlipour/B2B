from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import ApproverProfile, SalesmanProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:  # Approver
            ApproverProfile.objects.create(user=instance, department = "approvers_group")
        else:  # Salesman
            SalesmanProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'admin_profile'):
        instance.admin_profile.save()
    elif hasattr(instance, 'salesman_profile'):
        instance.salesman_profile.save()