from django.db import models

# Create your models here.

class table_so2(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"SO2 from {self.city}: {self.value} at {self.date}"

class table_h2s(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"H2S from {self.city}: {self.value} at {self.date}"
class table_no2(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"NO2 from {self.city}: {self.value} at {self.date}"

class table_nox(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"NOX from {self.city}: {self.value} at {self.date}"
class table_no(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"NO from {self.city}: {self.value} at {self.date}"
class table_co(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"CO from {self.city}: {self.value} at {self.date}"
class table_o3(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"03 from {self.city}: {self.value} at {self.date}"
class table_pm10(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"PM10 from {self.city}: {self.value} at {self.date}"
class table_pm25(models.Model):
    city=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    #duration=models.IntegerField()
    def __str__(self):
        return f"PM2.5 from {self.city}: {self.value} at {self.date}"
