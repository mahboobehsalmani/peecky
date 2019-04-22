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
        db_table = 'Contact_Number'

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

class BusinessInfo(models.Model):

    class Meta:
        db_table = 'Business_Info'

    id = models.CharField(max_length=64, primary_key=True)

    name = models.CharField(max_length=16)

    value = models.CharField(max_length=16)

class Has_Business_Info(models.Model):

    class Meta:
        db_table = 'Has_Business_Info'
    
    id = models.CharField(max_length=64, primary_key=True)

    info_id = models.ForeignKey('BusinessInfo', on_delete=models.CASCADE)

    business_id = models.ForeignKey('Business', on_delete=models.PROTECT)
    
class Interval(models.Model):

    class Meta:
        db_table = 'Interval'

    id = models.CharField(max_length=64, primary_key=True)

    from_time = models.CharField(max_length=8)

    till_time = models.CharField(max_length=8)

class Day(models.Model):

    class Meta:
        db_table = 'Day'
    
    id = models.CharField(max_length=64, primary_key=True)

class HasOpeningHour(models.Model):

    class Meta:
        db_table = 'Has_Opening_Hour'
    
    id = models.CharField(max_length=64, primary_key=True)

    day = models.ForeignKey('Day', on_delete=models.CASCADE)

    opening_hour = models.ForeignKey('Interval', on_delete=models.CASCADE)

class FoodRelated(models.Model):

    class Meta:
        db_table = 'Food_Related'

    id = models.OneToOneField( 'Business', on_delete=models.PROTECT, primary_key=True)

class MenuItem(models.Model):

    class Meta:
        db_table = 'Menu_Item'

    id = models.CharField(max_length=64, primary_key=True)

    name = models.CharField(max_length=32)
    
    price = models.CharField(max_length=32)

class Menu(models.Model):

    class Meta:
        db_table = 'Menu'

    id = models.CharField(max_length=64, primary_key=True)

    title = models.CharField(max_length=16)

class MenuHasItem(models.Model):

    class Meta:
        db_table = 'Menu_Hash_Item'

    id = models.CharField(max_length=64, primary_key=True)

    item_id = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Restaurant(models.Model):

    class Meta:
        db_table = 'Restaurant'

    id = models.OneToOneField( 'FoodRelated', on_delete=models.PROTECT, primary_key=True)

class CoffeeShop(models.Model):

    class Meta:
        db_table = 'Coffee_Shop'

    id = models.OneToOneField( 'FoodRelated', on_delete=models.PROTECT, primary_key=True)

class Reservable(models.Model):

    class Meta:
        db_table = 'Reservable'

    id = models.OneToOneField( 'Business', on_delete=models.PROTECT, primary_key=True)

class Hotel(models.Model):

    class Meta:
        db_table = 'Hotel'

    id = models.OneToOneField( 'Business', on_delete=models.PROTECT, primary_key=True) 