from django.core.management.base import BaseCommand

from api.models import SubjectStudent


class Command(BaseCommand):
    help = 'Create data for Subject Student Table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of students for creation')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            s = SubjectStudent.objects.create(
                subject_id=1,
                student_id=i+4
            )
            self.stdout.write(self.style.SUCCESS(f'Student with id: {s.id} was registered'))