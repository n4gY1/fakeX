from django import forms
from django.forms import ModelForm

from x.models import Logins


class LoginsForm(ModelForm):
    class Meta:
        model = Logins
        fields = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super(LoginsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control '
        self.fields['email'].widget.attrs['placeholder'] = "e-mail"
        self.fields['password'].widget.attrs['placeholder'] = "jelszó"
