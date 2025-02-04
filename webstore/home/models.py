from django.db import models

class Department(models.Model):
    DeptNumber = models.IntegerField(primary_key=True)
    DeptName = models.CharField(max_length=255)
    image_url = models.URLField(default='https://via.placeholder.com/300x200')

    def __str__(self):
        return f"{self.DeptNumber} - {self.DeptName}"  # Example: "1 - Arms"
    
    
class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True) #unique product id
    ProductName = models.CharField(max_length=255)
    ProductNumber = models.IntegerField() #number of products in stock
    ProductDate = models.DateField() #date in stock
    DeptNumber = models.ForeignKey(Department,on_delete=models.CASCADE,to_field='DeptNumber')

    def __str__(self):
        return f"{self.ProductName} - (#{self.ProductNumber})" # Example: "Gatling Gun - 40001111"
