from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Register
from app2.models import Register

@receiver(post_save, sender=Register)
def create_user(sender,instance,created, **kwatgs):
    if created:
        Register.objects.create(
            email=instance.email,
            password=instance.password
        )