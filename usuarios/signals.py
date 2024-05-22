from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PerfilUsuario
from django.dispatch import receiver
from datetime import datetime
from allauth.account.signals import user_logged_in
import os


@receiver(user_logged_in)
def create_user_profile(sender, request, user, **kwargs):
    # Verifica se o usuário fez login usando o Google
    if user.socialaccount_set.filter(provider='google').exists():
        # Verifica se o usuário já tem um perfil
        if not hasattr(user, 'perfilusuario'):
            # Se não tiver, cria um novo perfil
            PerfilUsuario.objects.create(
                usuario=user,
                nome=user.first_name if user.first_name else user.username,
                # Define a data de nascimento como primeiro de janeiro de 2000
                data_nascimento=datetime(2000, 1, 1),
                foto_perfil=None
            )

@receiver(pre_save, sender=PerfilUsuario)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = PerfilUsuario.objects.get(pk=instance.pk).foto_perfil
    except PerfilUsuario.DoesNotExist:
        return False

    new_image = instance.foto_perfil
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
