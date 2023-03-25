from account_module.models import User
from django import forms


class PersonalInfoForm(forms.Form):
    username = forms.CharField(max_length=100, label='username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'id': 'username',
        'disabled': 'disabled'
    }))
    first_name = forms.CharField(max_length=100, required=False, label='first_name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'id': 'first_name',
        'disabled': 'disabled'
    }))
    last_name = forms.CharField(max_length=100, required=False, label='last_name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'id': 'last_name',
        'disabled': 'disabled'
    }))
    phone_number = forms.CharField(max_length=100, required=False, label='phone_number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number',
        'id': 'phone_number',
        'disabled': 'disabled'
    }))
    location = forms.CharField(max_length=100, required=False, label='location', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location',
        'id': 'location',
        'disabled': 'disabled'
    }))
    status = forms.ChoiceField(required=False, choices=[('active', 'Active'), ('away', 'Away'),
                                        ('do not disturb', 'Do not disturb')],
                               widget=forms.Select(attrs={
                                   'class': 'form-control',
                                   'id': 'status',
                                   'disabled': 'disabled'
                               }))
    short_about_me = forms.CharField(max_length=300, required=False, label='short_about_me', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Short about me',
        'id': 'short_about_me',
        'disabled': 'disabled'
    }))
    about_me = forms.CharField(max_length=300, required=False, label='about_me', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'About me',
        'id': 'about_me',
        'disabled': 'disabled'
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
        self.fields['short_about_me'].initial = user.profile.short_about_me
        self.fields['about_me'].initial = user.profile.about_me

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exclude(id=self.id).first()
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
        user.profile.short_about_me = self.cleaned_data['short_about_me']
        user.profile.about_me = self.cleaned_data['about_me']
        user.save()
        return user
