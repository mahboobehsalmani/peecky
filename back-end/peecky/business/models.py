from django.db import models

class Business(models.Model):

    #meta data about the model
    class Meta:
        #table name
        db_table = 'Business'

    #primary key
    id = models.CharField(max_length=64, primary_key=True)

    #name of the business
    name = models.CharField(max_length=32)

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


class ContactNumber(models.Model):

    class Meta:
        db_table = 'ContactNumber'

    #primary key
    id = models.CharField(max_length=64, primary_key=True)

    #contact number
    number = models.CharField(max_length=16)

class Owns_Contact_Number(models.Model):

    class Meta:
        db_table = 'Owns_Contact_Number'
    
    id = models.CharField(max_length=64, primary_key=True)

    business_id = models.ForeignKey('Business', on_delete=models.PROTECT)

    contact_id = models.ForeignKey('ContactNumber', on_delete=models.PROTECT)

    status = models.IntegerField()
