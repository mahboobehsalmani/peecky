from django.db import models

# Create your models here.
class Business(models.Model):

    #meta data about the model
    class Meta:
        #table name
        db_table = 'Business'

    #primary key
    id = models.CharField(max_length=64, primary_key=True, blank=False)

    #name of the business
    name = models.CharField(max_length=32, blank=False)

    #website of the business
    website = models.CharField(max_length=32, blank=True, null=True)

    #address of the business
    address = models.CharField(max_length=128, blank=True, null=True)

    #description about business
    description = models.CharField(max_length=128, blank=True, null=True)

    #latitude of the business on map
    latitude = models.CharField(max_length=16, blank=True, null=True)

    #longitude of the business on map
    longitude = models.CharField(max_length=16, blank=True, null=True)

    status = models.IntegerField()