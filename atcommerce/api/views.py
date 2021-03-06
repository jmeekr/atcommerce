from django.shortcuts import render, reverse
from django import forms
from django.db import models

from .models import Customer, Product, Eorders, Records

from dateutil import parser

class RecordForms(forms.ModelForm):
    class Meta:
        model = Records
        fields = ('description', 'file')

class FileParser:
    """
    Row looks like
    id  first last      street          state zip   status  id  product price       date
    1	Snake	Plisken	123 Fake St.	AZ	12345	new	    432	Masthead	100.12	2007-04-05T14:30Z
    """
    def __init__(self, file_):
        self.raw_file = file_
        self.file = file_.read().decode('utf8')
        self.rows = self.file.split('\n')
        self.headers = [
            'customer_id',
            'first_name',
            'last_name',
            'street_address',
            'state',
            'zip_code',
            'purchase_status',
            'product_id',
            'name', # product name in Product
            'purchase_amount',
            'order_date',
        ]

    def parse_file(self):
        for row in self.rows:
            cells = row.split('\t')
            row_tuple = zip(self.headers, cells)
            row_dict = {k:v for k, v in row_tuple}
            # Conver isoformat to python date time object for storage
            row_dict.update({'order_date' : parser.parse(row_dict.get('order_date'))})

            prod, prod_created = Product.objects.update_or_create(
                id = row_dict.get('product_id'),
                defaults = {
                    'name' : row_dict.get('name'),
                    # description is not implemented
                }
            )

            cust, cust_created = Customer.objects.update_or_create(
                id = row_dict.get('customer_id'),
                defaults = {
                    'first_name' : row_dict.get('first_name'),
                    'last_name' : row_dict.get('last_name'),
                    'street_address' : row_dict.get('street_address'),
                    'state' : row_dict.get('state'),
                    'zip_code' : row_dict.get('zip_code'),
                }
            )

            if prod_created or cust_created:
                print('new record for Eorders')

            # Suppose that a custom may have more than one transaction on the
            # same product, we don't get a new id for that transaction
            # so we can also use the datetime for that interaction
            # Say person A buys item I every Monday
            # Unfortunately we cannot make this assumption based on the
            # order_date because cancellations happen in the future
            try:
                exists = Eorders.objects.get(
                   (models.Q(product__id = prod.id) &
                    models.Q(customer__id = cust.id)),
                )

                # If it does not throw an Exception it exists,
                # and we should try to update it
                # This was replaced from create_or_update because of an error
                # with the syntax

                exists.purchase_status = row_dict.get('purchase_status')
                exists.purchase_amount = row_dict.get('purchase_amount')
                exists.order_date = row_dict.get('order_date')
                exists.save()
                print('updated record')

            except Eorders.DoesNotExist:
                print('records does not exist... create it')
                eorder = Eorders.objects.create(
                    product = prod,
                    customer= cust,
                    #order_date = row_dict.get('order_date'),
                    purchase_status = row_dict.get('purchase_status'),
                    purchase_amount = row_dict.get('purchase_amount'),
                    order_date = row_dict.get('order_date')
                )
                print('created record')

def upload_file(request):
    form = RecordForms()
    if request.POST:
        print('receiving post')
        user = request.user.username
        file_ = request.FILES.get('file')
        file_name = file_.name
        description = request.POST.get('description')
        if file_:
            file_parser = FileParser(file_)
            file_parser.parse_file()

    return render(request, 'upload.html', {'form' : form})
