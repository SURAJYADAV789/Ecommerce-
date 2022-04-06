from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms
from crispy_forms.helper import FormHelper


class CustomerForm(UserCreationForm):
  
  password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password'}))
  password2 = forms.CharField(label='Confirm password',  widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Confirm Password'}))
    
  def _init_(self, *args, **kwargs):
    super(CustomerForm, self)._init_(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False 
  
  class Meta:
    
    model = MyUser
    fields = ('first_name','last_name','contact','email','password1','password2')
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Last Name'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact Number'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
     
    }

class BusinessForm(UserCreationForm):
  
  password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password'}))
  password2 = forms.CharField(label='Confirm password',  widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Confirm Password'}))
    
  def _init_(self, *args, **kwargs):
    super(BusinessForm, self)._init_(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False 
  
  class Meta:
    
    model = MyUser
    fields = ('first_name','last_name','contact','email','password1','password2')
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Last Name'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact Number'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
     
    }
