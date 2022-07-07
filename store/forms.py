from django import forms
from .models import Product



TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
       
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'digital':forms.Select(choices=TRUE_FALSE_CHOICES),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
