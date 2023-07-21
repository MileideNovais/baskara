from django import forms


class UserForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()