from django.shortcuts import render

from django import forms
from django.db import models
from .models import Customer, Product, Eorders, Records

class RecordForms(forms.ModelForm):
    class Meta:
        model = Records
        fields = ('description', 'file')

class parse_file:
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
        for row in rows:
            cells = row.split('\t')
            row_tuple = zip(self.headers, cells)
            row_dict = {k:v for k, v in row_tuple}


def upload_file(request):
    form = RecordForms()
    if request.POST:
        user = request.user.username
        file_ = request.FILES.get('file')
        file_name = file_.name
        description = request.POST.get('description')
        if file_:
            parse_file(file_)

    if request.GET:
        pass
    return render(request, 'upload.html', {'form' : form})
