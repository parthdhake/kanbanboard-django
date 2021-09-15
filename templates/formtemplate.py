from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from home.models import Board, Card


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    fullname = forms.CharField(label="Full name")

    class Meta:
        model = User
        fields = (
            "fullname",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'content', 'priority', 'status']

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})