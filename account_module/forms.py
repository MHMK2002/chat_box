import re

from django import forms

from account_module.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your username',
        'id': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your email',
        'id': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your password',
        'id': 'password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password',
        'id': 'confirm_password'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_$!%*?&])[A-Za-z\d@$_!%*?&]{8,}$'
        if re.match(regex, password) is None:
            raise forms.ValidationError('Password must contain at least 8 characters,'
                                        ' 1 uppercase, 1 lowercase,'
                                        ' 1 number and 1 special character')
        return confirm_password

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user


class ProfileForm(forms.Form):
    def __init__(self, id):
        super().__init__()
        self.id = id

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'inputFirstName',
        'placeholder': 'Enter your first name',
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'inputLastName',
        'placeholder': 'Enter your last name',
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'inputUsername',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'inputEmailAddress',
        'placeholder': 'Enter your email address',
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.id).exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.id).exists():
            raise forms.ValidationError('Email is already taken')
        return email

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        user = User.objects.get(id=self.id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        return user


class UserAvatarForm(forms.Form):
    avatar = forms.ImageField(required=False, max_length=5 * 1024 * 1024
                              , widget=forms.FileInput(attrs={
                                'class': 'custom-file-input',
                                'id': 'inputGroupFile01',
                            }))
