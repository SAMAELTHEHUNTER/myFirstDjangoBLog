from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', error_messages={'required':'this username is taken.please try another one'}, max_length=20, help_text='enter your username')
    password1 = forms.CharField(label='password', error_messages={'required':'this is not strong enogh'}, max_length=254, help_text='password should iclude one digits and one word')
    password2 = forms.CharField(label='confirmpassword', error_messages={'required':'its not match'}, max_length=254, help_text='retype your password')
    phone_number = forms.IntegerField(label='phone_number' ,max_value=9999999999,  min_value=1000000000, error_messages={'required':'its wrong'}, required=False, help_text='enter your phone number')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2',)
