from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


class SongForm(forms.Form):
    file_type = forms.CharField(
        label='FileType', max_length=5, min_length=1)
    title = forms.CharField(label='Title', max_length=25,
                            min_length=1)
    stars = forms.IntegerField(
        label='Stars (0 to 5)', max_value=5, min_value=1)
    favourite = forms.BooleanField(label='Favourite')

    file_type.widget.attrs.update({'class': 'form-control'})
    title.widget.attrs.update({'class': 'form-control'})
    stars.widget.attrs.update({'class': 'form-control'})
