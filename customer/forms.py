from django import forms

from .models import Customer

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField()
    area_code = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    address_number = forms.CharField()
    class_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    evolution_field = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone",
            "address",
            "address_number",
            "class_time",
            "evolution_field",
        )