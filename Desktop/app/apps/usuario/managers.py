from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self,nombre,apellido,username, email, password, **extra_fields):
        if not email:
            raise ValueError(_('El e-mail es obligatorio'))
        elif not username:
            raise ValueError(_('El nombre de usuario es obligatorio'))
        extra_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(nombre=nombre,apellido=apellido,username= username,correoElectronico=email,password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('has_module_perms',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(None,None,username,'superuser2@admin.cl', password, **extra_fields)

    # def get_user(self,username=None,email=None ):
    #     try:
    #         if Perfil.objects.get(username = username):
    #             return ValidationError( _('nombre de usuario no disponible'),params={'username': username})
    #         elif Perfil.objects.get(correoElectronico = email):
    #             return ValidationError( _('correo electronico no disponible'),params={'correoElectronico': email})
    #     except Perfil.DoesNotExist:
    #         return None
