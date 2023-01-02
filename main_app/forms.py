# from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Restaurant

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=254, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # print(forms)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UpdateRestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    menu = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    hours = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'menu', 'hours']
