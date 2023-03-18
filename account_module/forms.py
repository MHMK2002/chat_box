import re

from django import forms

from account_module.models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Type your first name'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Type your last name'
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Type your username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input100',
        'placeholder': 'Type your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
        'placeholder': 'Type your password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
        'placeholder': 'Confirm your password'
    }))


    def clean(self):
        # 1. Get data from form
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        # 2. Check password and confirm_password
        if password != confirm_password:
            raise forms.ValidationError('Password and confirm password does not match')
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
        if re.match(regex, password) is None:
            raise forms.ValidationError('Password must contain at least 8 characters,'
                                        ' 1 uppercase, 1 lowercase and 1 number')
        # 3. Check username
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already exists')
        # 4. Check email
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already exists')

        return cleaned_data

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        return user
