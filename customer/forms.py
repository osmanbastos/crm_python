from django import forms

from .models import Customer

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EmailInput(forms.EmailInput):
    input_type = 'email'
class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={'max_length': 'Não pode ter mais de 30 caracteres'},
        )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={'max_length': 'Não pode ter mais de 50 caracteres'},
        )
    email = forms.EmailField(label="E-mail", widget=EmailInput())
    birth_date = forms.DateField(label="Data de nascimento", widget=DateInput())
    cpf_field = forms.RegexField(
        label="CPF",
        regex=r'^\+?1?[0-9]{11}$',
        error_messages={'invalid': 'Digite um CPF válido'}
    )
    area_code = forms.RegexField(
        label="DDD",
        regex=r'^\+?1?[0-9]{2}$',
        error_messages={'invalid': 'Digite um DDD válido'}
    )
    phone = forms.RegexField(
        label="Telefone",
        regex=r'^\+?1?[0-9]{9}$',
        error_messages={'invalid': 'Digite um telefone válido'},
        widget=forms.TextInput(attrs={'placeholder': "Digite o CPF sem pontos ou traços"})
    )
    address = forms.CharField(label="Endereço")
    address_number = forms.CharField(label="CEP")
    class_time = forms.TimeField(widget=TimeInput(format='%H:%M'), label="Horário da aula")
    active = forms.RadioSelect()
    evolution_field = forms.CharField(label="Observações", widget=forms.Textarea)

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "cpf_field",
            "birth_date",
            "area_code",
            "phone",
            "address",
            "address_number",
            "class_time",
            "active",
            "evolution_field",
        )