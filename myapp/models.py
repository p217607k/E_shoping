
from email.policy import default
from random import choices
from secrets import choice
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
import  datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sub_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Product(models.Model):
    Available =(
        ('In stack','In stack'),
        ('Out of stack','Out of stack')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    available  = models.CharField(max_length = 100,choices =Available,null ='True')
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Ecommerce/ping')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,label = "Email" ,error_messages={'Exists': 'this is massage all ready Exists'})
    fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['fullname'].widget.attrs['placeholder'] = 'fullname'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm_password'


    def save(self, commit=True):

        user = super(RegisterForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

  
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class contect_us(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField(max_length =100)
    subject = models.TextField(max_length =100)
    message=models.TextField(max_length =1000)
    def __str__(self):
        return self.name
class Order(models.Model):
    image = models.ImageField(upload_to = 'Ecommerce/Order')
    product = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    price = models.IntegerField(max_length =100,default='')
    quantity = models.IntegerField(max_length =100)
    total = models.CharField(max_length =100,default='')
    address = models.CharField(max_length =100)
    phone = models.CharField(max_length =100)
    pincode = models.CharField(max_length =10)
    datetime = models.DateField(default=datetime.date.today())
    def __str__(self):
        return self.phone