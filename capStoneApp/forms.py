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
    service_name = forms.CharField(label="Service Name", max_length=100)
    service_price = forms.DecimalField(
        label="Service Price ($)", decimal_places=2, min_value=0.01
    )
    additional_comments = forms.CharField(
        label="Additional Comments", widget=forms.Textarea
    )
