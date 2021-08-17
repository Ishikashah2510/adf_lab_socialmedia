from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    birthdate = models.DateTimeField(blank=True)
    mobile_no = models.IntegerField(unique=True)
    password = models.CharField(max_length=25)
