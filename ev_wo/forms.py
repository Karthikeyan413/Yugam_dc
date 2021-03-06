from django import forms
from django.contrib.auth.models import User
from ev_wo.models import org,events
from django.core import validators


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Username',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'user@mail.com',
        }
    ))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input',
        }
    ))

    class Meta():
        model = User
        fields = ['username', 'password', 'email']

class EventImage(forms.ModelForm): 

    event_poster = forms.ImageField()
    class meta:   
        models = events 
        fields = 'event_poster'  