from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, \
    CheckboxInput, TextInput, EmailInput, Form


class RegistrationForm(ModelForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'input-xlarge', 'required': 'true',
               'placeholder': 'John Doe'}), required=True)
    email = CharField(widget=EmailInput(attrs={'class': 'input-xlarge',
                                               'autofocus': 'autofocus',
                                               'required': 'true',
                                               'placeholder': 'Email Address'}),
                      required=True)
    password = CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-xlarge', 'required': 'true'}), required=True)
    re_password = CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-xlarge', 'required': 'true'}), required=True)
    remember_me = CheckboxInput()

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password','')
        re_password = cleaned_data.get('re_password','')
        if password != re_password:
            raise forms.ValidationError('Password and confirm password should match !!')
        return super(RegistrationForm, self).clean()


    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(Form):
    username = CharField(widget=TextInput(
        attrs={'class': 'input-xlarge', 'required': 'true',
               'placeholder': 'John Doe'}), required=True)
    password = CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-xlarge', 'required': 'true'}), required=True)




