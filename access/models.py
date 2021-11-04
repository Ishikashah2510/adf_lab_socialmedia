from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone

# Create your models here.


class users(AbstractBaseUser):
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
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=25)
    is_authenticatedd = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'birthdate', 'gender',
                       'mobile_no', 'password']

    class Meta:
        permissions = [
            ("can_post", "The user can make a post"),
            ("can_delete_account", "The user can delete their account"),
        ]
