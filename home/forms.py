from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User
from .models import Masyli, SupernaturalAbilities
from django.core.exceptions import ValidationError


class MasyliConfirmDelete(forms.Form):
    confirm_delete = forms.BooleanField(required=False)

    def clean(self):
        if self.cleaned_data["confirm_delete"] is False:
            raise ValidationError("You must confirm this form!")
        return super(MasyliConfirmDelete, self).clean()


class MasyliForm(forms.ModelForm):
    class Meta:
        model = Masyli
        fields = ['name', 'age', 'color', 'origin', 'photo']


class SupernaturalForm(forms.ModelForm):
    class Meta:
        model = SupernaturalAbilities
        fields = ['masyli', 'ability_name', 'description', 'photo']


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )
