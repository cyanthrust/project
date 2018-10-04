from django.db import models
from django.utils import timezone

# Create your models here.

class Character(models.Model):
    JOBS = (
        ('HM', 'Headmaster'),
        ('MM', 'Management'),
        ('PT', 'Plot'),
        ('NU', 'Normal User'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=16, blank=False)
    middlename = models.CharField(max_length=16, blank=True)
    lastname = models.CharField(max_length=16, blank=False)
    created_date = models.DateTimeField(default=timezone.now())
    last_login = models.DateTimeField(default=timezone.now())
    birthday = models.DateField(blank=False)
    ip_adress = models.GenericIPAddressField(default="0.0.0.0")
    jobs = models.CharField(max_length=2, choices=JOBS, default='NU')

    def __str__(self):
        return self.firstname

class active_Character(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, unique=True,)
    char = models.ForeignKey('Character', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

