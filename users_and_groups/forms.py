from .models import Group, User
from django.forms import ModelForm, TextInput, Textarea, Select


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name", "desc"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Group name"
            }),
            "descr": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description"
            })
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "groups"]

        widgets = {
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "User name"
            }),
            "groups": Select(attrs={
                "class": "form-control",
                "placeholder": "Select group"
            })
        }