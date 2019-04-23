from django.db import models

# Create your models here.
class contact_number(models.Model):
    number = models.CharField(max_length=16)