from django.forms import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput())