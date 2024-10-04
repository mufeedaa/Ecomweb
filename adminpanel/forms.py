from django import forms
from home.models import Product, Category, User
import re
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    name = forms.CharField(label= 'Product Name', widget=forms.TextInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter the product name'
    }))
    description = forms.CharField(label = 'Product Details', widget = forms.Textarea(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter the product details'

    }))
    image = forms.ImageField(label= 'Product Image', widget = forms.ClearableFileInput(attrs={
        'Class': 'form-controle',
        
    }))
    category = forms.ModelChoiceField(label= 'category name',queryset=Category.objects.all(), widget= forms.Select(attrs={
        'Class': 'form-controle',
     }))
    price = forms.IntegerField(label = 'Rate', widget = forms.NumberInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter the rate of product'
    }))
    stock = forms.IntegerField(label = 'Quantity available', widget = forms.NumberInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter the quantity'
    }))
    class Meta:
        model = Product 
        fields = '__all__'
        # fields = ['name','description']
        # exclude = ['stock']
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if(len(name) < 10 ):
            return self.add_error('name', 'Name should have atleast 10 charaters')



class CategoryForm(forms.ModelForm):
    name = forms.CharField(label= 'Category Name', widget=forms.TextInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter the category name'
    }))
    class Meta:
        model = Category
        fields = '__all__'      


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label= 'first Name', widget=forms.TextInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your first name'
    }))
    last_name = forms.CharField(label= 'last Name', widget=forms.TextInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your last name'
    }))
    username = forms.CharField(label= 'userName', widget=forms.TextInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your username'
    }))
    email = forms.CharField(label= 'email', widget=forms.EmailInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your email address'
    }))
    password1 = forms.CharField(label= 'password', widget=forms.PasswordInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(label= 'password', widget=forms.PasswordInput(attrs={
        'Class': 'form-controle',
        'placeholder': 'Enter your password'
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1','password2' ]




class LoginForm(forms.Form):
    username = forms.CharField(label = 'username',max_length=100,required = True,
     widget = forms.TextInput(attrs={
        'class':'form-controle', 'placeholder':'Enter your username'
    }))   
    password = forms.CharField(label = 'password',max_length=100,required = True,
     widget = forms.PasswordInput(attrs={
        'class':'form-controle', 'placeholder':'Enter your password'
    }))      