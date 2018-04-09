from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.
"""

    # Autoincrement int in Django by default
    Customer id (an integer)
    Customer first name
    Customer last name
    Customer street address (assume US addresses only)
    Customer state (assume US addresses only)
    Customer zip code (assume US addresses only)

    Change in purchase status - this will be either 'new' or 'canceled'
    Product id for purchase (an integer)
    Product name (a string, not longer than 100 characters)
    Product purchase amount (in US dollars)
    Date and time in ISO8601 format, i.e. 2007-04-05T14:30Z

"""

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=80)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    # Even though we're assuming US based addresses,
    # Other countries have alphanumeric zip codes,
    # and US based zipcodes can be 9 characters, so we'll
    # assume up to 20 charactes can be used

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Eorders(models.Model):
    customer = models.ForeignKey(Customer, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT)
    purchase_status = models.CharField(
        max_length=3,
        choices=(('NEW', 'New Order'), ('CXL','Canceled Order')),
        default='NEW',
    )

    # Amount could be different based on orders? So in this table rather than
    # product price in Product table
    purchase_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    order_date = models.DateTimeField()

class Records(models.Model):
    uploaded_by = models.CharField(max_length=80)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='records/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
