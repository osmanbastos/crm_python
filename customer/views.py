from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerForm

# Create your views here.
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all() #mostrar todos os registros

class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)