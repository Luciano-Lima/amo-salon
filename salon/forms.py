from  django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, EmailValidator, RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(validators=[MinLengthValidator(3, 'Needs to be at least 3 characters long! '), RegexValidator(r'^[a-zA-Z]*$', 'That is not a valid name.')], max_length=100)
    email = forms.EmailField(validators=[EmailValidator])
    message = forms.CharField(validators=[MinLengthValidator(20, 'Needs to be at least 20 characters long! '),], widget=forms.Textarea)

    