from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=20)
    pass1 = models.CharField(max_length=20)
    date = models.DateField()