from django.core.management.base import BaseCommand, CommandError
from _app_pollution_1.models import *
from _app_pollution_1.scrapp_data import *

class Command(BaseCommand):
    help = 'Obrisi sve podatke koristeci django ORM'

    def handle(self, *args, **options):
      self.stdout.write(self.style.SUCCESS("Brisanje u toku: "))
      table_co.objects.all().delete()
      table_h2s.objects.all().delete()
      table_no.objects.all().delete()
      table_no2.objects.all().delete()
      table_nox.objects.all().delete()
      table_o3.objects.all().delete()
      table_pm10.objects.all().delete()
      table_pm25.objects.all().delete()
      table_so2.objects.all().delete()
      self.stdout.write(self.style.SUCCESS("Gotovo"))
    
