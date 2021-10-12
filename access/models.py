from django.db import models
from django.utils import timezone

# Create your models here.


class users(models.Model):
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Others'),
        ('Not specified', 'Do not wish to specify')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=15,
                              choices=genders,
                              default='Female')
    mobile_no = models.IntegerField(unique=True)
    pro_pic = models.ImageField(upload_to='profile_photos/',
                                default='/profile_photos/default_pic.jpg')
    acc_creation_date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)

    def is_user_authenticated(self, yes=True):
        self.is_authenticated = yes
