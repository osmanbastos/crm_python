from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField()
    area_code = models.CharField(max_length=2)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    address_number = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class_time = models.TimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = 'customer'
        