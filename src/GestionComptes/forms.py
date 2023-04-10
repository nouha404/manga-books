from django import forms


class Inscription(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
