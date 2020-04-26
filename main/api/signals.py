from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subject, TeacherSubject


@receiver(post_save, sender=Subject)
def user_created(sender, instance, created, **kwargs):
    if created:
        # TeacherSubject.objects.create(teacher=instance)
        print(kwargs)
