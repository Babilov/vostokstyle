from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label='Почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    email = forms.CharField(label='Почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

