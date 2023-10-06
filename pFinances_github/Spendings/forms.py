from django import forms
from .models import *
from datetime import date

#Here you can create your forms

class ExpenseTypeForm(forms.ModelForm):
    name = models
    
    class Meta:
        model = ExpenseType
        fields = ('type',)

        widgets = {
            'type' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter an expense type'}),
        }

class ExpenseForm(forms.ModelForm):
    name = models

    class Meta:
        model = Expense
        fields = ('cost', 'type', 'date')

        widgets = {
            'cost' : forms.NumberInput(attrs={'class':'form-control'}),
            'type' : forms.Select(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control', 'type':'date' }) 
        }


