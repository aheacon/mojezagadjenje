from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Testing the hello CLI'

    def add_arguments(self, parser):
      # Optional --name
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
      self.stdout.write(self.style.SUCCESS('Hello from CLI "%s"' % options['name']))


