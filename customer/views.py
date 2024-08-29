from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 8
    model = Customer
    #queryset = Customer.objects.all() # mostrar todos os registros
    # Busca por first_name e last_name
    def get_queryset(self):
        query = self.request.GET.get("name")
        class_time = self.request.GET.get("class_time")
        queryset = Customer.objects.all()
        if query:
            return Customer.objects.filter(first_name__icontains=query) | Customer.objects.filter(last_name__icontains=query) | Customer.objects.filter(email__icontains=query) | Customer.objects.filter(phone__icontains=query)
        if class_time:
            return Customer.objects.filter(class_time__icontains=class_time)
        return Customer.objects.all()

class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("customer:customer-list")
    
class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm
    model = Customer
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("customer:customer-list")
    
class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)
    
    def get_success_url(self):
        return reverse_lazy("customer:customer-list")