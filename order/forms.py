from django import forms
from .models import Order,Category

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'poster_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'is_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_digital': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    # Define choices for the category field
    category = forms.ChoiceField(choices=Order.category)