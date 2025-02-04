from django.contrib import admin
from .models import Product #imports class
from .models import Department #imports class


# Register your models here.
admin.site.register(Department) #allows admin to add Department class data fields
admin.site.register(Product) #allows admin to add Product class data fields