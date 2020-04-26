import random

from django.core.management.base import BaseCommand

from api.models import Subject


class Command(BaseCommand):
    help = 'Create data for Subject Table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of subjects for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new products')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = 'CS'

        for i in range(total):
            s = Subject.objects.create(name=f'calculus {i+1}',
                                       course_code=f'{prefix}{random.randint(1000, 4000)}',
                                       description=f'subject with index: {i}')
            self.stdout.write(self.style.SUCCESS(f'Subject with id: {s.id} was created'))
