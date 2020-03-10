from django.core.management.base import BaseCommand, CommandError
from _app_pollution_1.models import *
from _app_pollution_1.scrapp_data import *
import datetime

class Command(BaseCommand):
    help = 'Pokreni cron job svakih sat vremena da dobijemo i spasimo podatke u \
            bazu podataka'

    def handle(self, *args, **options):
      # Trenutno scrap_aqi() scrappira podatke za Zenicu
      # Potrebno je doraditi da scrappira podatke za ostale gradove,
      gradovi=scrap_aqi()
      for (lokacija, array_0) in gradovi.items():
        self.stdout.write(self.style.SUCCESS(lokacija))
        #self.stdout.write(self.style.SUCCESS(type(array_0))) # <class 'list'>
        for _dict in array_0: # iterate through list
          for key in _dict: # iterate through dictionaries
            self.stdout.write(self.style.SUCCESS(key+" "+_dict[key]))
            '''
            Save into database: 
            - missing city (@todo),
            - lokacija, 
            - check_key,
            - value
            See example of output bellow
            '''
            # value can be empty string or #(no measurments)
            if (_dict[key] == '#'):
              myval=0
            else:
              myval= int(_dict[key] or 0)
            if (key == 'so2'):
              row=table_so2( city="Zenica", location=lokacija, value=myval)
            elif (key == 'h2s'):
              row=table_h2s( city="Zenica", location=lokacija, value=myval)
            elif (key == 'no2'):
              row=table_no2( city="Zenica", location=lokacija, value=myval)
            elif (key == 'nox'):
              row=table_nox( city="Zenica", location=lokacija, value=myval)
            elif (key == 'no'):
              row=table_no( city="Zenica", location=lokacija, value=myval)
            elif (key == 'co'):
              row=table_co( city="Zenica", location=lokacija, value=myval)
            elif (key == 'o3'):
              row=table_o3( city="Zenica", location=lokacija, value=myval)
            elif (key == 'pm10'):
              row=table_pm10( city="Zenica", location=lokacija, value=myval)
            elif (key == 'pm2.5'):
              row=table_pm25( city="Zenica", location=lokacija, value=myval)

            row.save()

      # Alarm check for latest n value for each location
      #n=3
      #for i in table_co.objects.filter(location='Brist')[:n]

      # 

    '''
    Example of output:
    Brist
    so2 27
    h2s 
    no2 14
    nox 19
    no 5
    co 
    o3 74
    pm10 65
    pm2.5 
    '''
    
