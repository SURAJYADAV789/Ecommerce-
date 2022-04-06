from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        
        fields='__all__'
        widgets={
            'p_name':forms.TextInput(attrs={'class':'form-control '}),
            'p_price':forms.NumberInput(attrs={'class':'form-control'}),
            'p_desc':forms.Textarea(attrs={'class':'form-control'})
            
        }