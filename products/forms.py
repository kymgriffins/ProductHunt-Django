from django import forms
from .models import Product
from django.forms import ModelForm
from django.utils import timezone
import datetime
class ProductForm(forms.ModelForm):
    class  Meta:
       model = Product
       exclude = ('pub_date','hunter','votes_total')



            