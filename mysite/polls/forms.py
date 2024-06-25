from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'password']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise ValidationError("Name cannot contain numbers")
        return name

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if any(char.isdigit() for char in surname):
            raise ValidationError("Surname cannot contain numbers")
        return surname

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('name') or not cleaned_data.get('surname') or not cleaned_data.get('username') or not cleaned_data.get('password'):
            raise ValidationError("All fields are required")
        return cleaned_data