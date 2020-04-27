import random

from django.core.management.base import BaseCommand

from users.models import MyUser


class Command(BaseCommand):
    help = 'Create data for Student Table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of students for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix student username')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = '17BD'

        for i in range(total):
            s = MyUser.objects.create(
                username=f"{prefix}_{random.randint(10000, 40000)}",
                email=f"student{i}@kbtu.kz",
                password="Django2020",
                role=2
            )
            self.stdout.write(self.style.SUCCESS(f'Student with id: {s.id} was created'))