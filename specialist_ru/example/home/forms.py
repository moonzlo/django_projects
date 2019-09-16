from django import forms

class LoginForms(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password')