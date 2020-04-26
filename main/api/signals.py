from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subject, News


@receiver(post_save, sender=Subject)
def user_created(sender, instance, created, **kwargs):
    if created:
        News.objects.create(title=f'{instance} was opened')
        print(kwargs)
