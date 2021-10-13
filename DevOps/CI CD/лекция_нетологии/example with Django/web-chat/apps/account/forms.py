from django import forms
from django_registration.forms import RegistrationForm

from apps.account.models import User


class RegisterForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name')
