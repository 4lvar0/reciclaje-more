from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Perfil
from django import forms
from django.contrib.auth import get_user_model


class CustomCreationForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('nombre','apellido','correoElectronico','username','password')
        
    def save(self, commit=True):
        user = super(CustomCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
    def is_valid(self):
        valid = super(CustomCreationForm,self).is_valid()
        if valid:
            return True
        else:
            return False
        

class ResetPasswordForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('correoElectronico',)