from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app_users.models import Profile


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

class AboutMeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)

class TopUpYourBalancetForm(forms.Form):
    amount_of_money = forms.FloatField()
