from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User

from .models import Customer



class CustomerForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Name'})
    mobileno = forms.CharField(error_messages={'requird':'Enter mobile no'})
    email = forms.CharField(error_messages={'requird':'Enter email '})
   # message = forms.CharField(error_messages={'requird':'Enter message '})
    message = forms.CharField(error_messages={'requird':'Enter message '},widget=forms.Textarea(attrs={'cols': 50, 'rows': 7}))


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus ':'true','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))






class CustomerRegistrationForm(UserCreationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'true','class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =['username','email','password1','password2']



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='old Password', widget=forms.PasswordInput(attrs={'autofocus ':'True', 'autocomplete' :'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus ':'True', 'autocomplete' :'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus ':'True', 'autocomplete' :'current-password','class':'form-control'}))





class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={ 'autocomplete' :'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={ 'autocomplete' :'current-password','class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name','locality','city','mobile','state','zipcode']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),


        }