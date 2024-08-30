from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField()
    cpf_field = models.CharField(max_length=11, unique=True, blank=True, null=True)
    area_code = models.CharField(max_length=2)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    address_number = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class_time = models.CharField(max_length=8, default='00:00')
    active = models.BooleanField(default=True)
    evolution_field = models.CharField(max_length=500, blank=True, null=True)
    evolution_updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_full_phone(self):
        return '(' + self.area_code + ') ' + self.phone
    
    def get_full_evolution(self):
        return self.evolution_updated.strftime('%d/%m/%Y %H:%M')

    def get_absolute_url(self):
        return reverse('customer:customer-update', kwargs={'id': self.id})
    
    def get_delete_url(self):
        return reverse('customer:customer-delete', kwargs={'id': self.id})

    class Meta:
        db_table = 'customer'
        