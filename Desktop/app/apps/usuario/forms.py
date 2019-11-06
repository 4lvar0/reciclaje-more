from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Perfil


class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Perfil
        fields = {'nombre','apellido','correoElectronico','username','password'}
    def save(self, commit=True):
        user = super(CustomCreationForm, self).save(commit=False)
        if commit:
            user.save()

        return user

class ResetPasswordForm(UserChangeForm):

    class Meta:
        model = Perfil
        fields = ('correoElectronico',)