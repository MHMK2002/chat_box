from account_module.models import User
from django import forms


class PersonalInfoForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'disabled': 'disabled',
        'id': 'username'
    }))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'disabled': 'disabled',
        'id': 'first_name'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'disabled': 'disabled',
        'id': 'last_name'
    }))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number',
        'disabled': 'disabled',
        'id': 'phone_number'
    }))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location',
        'disabled': 'disabled',
        'id': 'location'
    }))
    status = forms.ChoiceField(choices=[('active', 'Active'), ('away', 'Away'),
                                        ('do not disturb', 'Do not disturb')],
                               widget=forms.Select(attrs={
                                   'class': 'form-control',
                                   'id': 'status'
                               }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'profile-img-file-input',
        'id': 'profile-img-file-input',
        'type': 'file',
    }))

    short_about_me = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Short about me',
        'disabled': 'disabled',
        'id': 'short_about_me'
    }))
    about_me = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'About me',
        'disabled': 'disabled',
        'id': 'about_me'
    }))

    def __init__(self, id, data=None):
        super().__init__(data=data)
        self.id = id
        user = User.objects.get(id=id)
        self.fields['username'].initial = user.username
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['phone_number'].initial = user.profile.phone_number
        self.fields['location'].initial = user.profile.location
        self.fields['status'].initial = user.profile.status
        self.fields['avatar'].initial = user.profile.avatar
        self.fields['short_about_me'].initial = user.profile.short_about_me
        self.fields['about_me'].initial = user.profile.about_me

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exclude(id=self.id)
        if user is None:
            return username
        raise forms.ValidationError('Username already exists')

    def save(self):
        user = User.objects.get(id=self.id)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profile.phone_number = self.cleaned_data['phone_number']
        user.profile.location = self.cleaned_data['location']
        user.profile.status = self.cleaned_data['status']
        user.profile.avatar = self.cleaned_data['avatar']
        user.profile.short_about_me = self.cleaned_data['short_about_me']
        user.profile.about_me = self.cleaned_data['about_me']
        user.profile.save()
        return user
