from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "text"]


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = CreateCard
        fields = "__all__"


class InvoiceForm(forms.Form):
    description = forms.CharField(max_length=200)
    amount = forms.DecimalField()
