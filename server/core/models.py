# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# https://www.techiediaries.com/django-rest-framework-angular-2-part-3/
# Users can create products ,families ,locations and add transactions .
# A product belongs to a family of products and has a location .
# To move products out or in the stock we use make a transaction .



# A Product has these attributes : Title ,Description ,Unit Price ,SKU (Stock Keeping Unit) , Barcode (ISBN, UPC etc.) ,Quantity ,minQuantity ,Unit .
class Product(models.Model):

    sku = models.CharField(max_length=13,help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13,help_text="Enter Product Barcode (ISBN, UPC ...)")

    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Description")


    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.title

