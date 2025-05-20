from django import forms
from .models import Contract, Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']
        widgets = {
            'phone': forms.TextInput(attrs={'type': 'tel'}),
            'email': forms.EmailInput()
        }

class ContractForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.IntegerField(label='Телефон')
    email = forms.EmailField(label='Email')
    payment_method = forms.ChoiceField(
        label='Способ оплаты',
        choices=Contract.PAYMENT_METHODS,
        initial='card'
    )