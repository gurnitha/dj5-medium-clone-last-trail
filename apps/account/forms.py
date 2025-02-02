# apps/account/forms.py

# Django modules
from django import forms
from django.core import validators

# Third party modules
from tinymce.widgets import TinyMCE

# My modules
from account.models import Profile


class ProfileModelForm(forms.ModelForm):
	
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'instagram',
            'info',
        ]