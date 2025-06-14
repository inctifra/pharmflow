from django import forms
from .models import Drug, Stock, Dispensed

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'description', 'price']
        

class StockForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Stock
        fields = ['drug', 'batch_number', 'quantity', 'expiry_date']

class DispenseForm(forms.ModelForm):
    class Meta:
        model = Dispensed
        fields = ['stock', 'quantity', 'recipient', 'dispensed_by']
        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'recipient': forms.TextInput(attrs={'class': 'form-control'}),
            'dispensed_by': forms.TextInput(attrs={'class': 'form-control'}),
        }