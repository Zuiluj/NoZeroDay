from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class UpdateUser(forms.ModelForm):
    name = forms.CharField(required=False)
    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['name', ]

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password1', 'password2', ]

class CustomUserChange(UserChangeForm):
    
    class Meta:
        model = User
        fields = '__all__'
