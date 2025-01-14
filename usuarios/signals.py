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
    if not instance.pk:  # Se o objeto é novo, não há imagem antiga para deletar
        return

    try:
        # Recupera a instância do banco de dados antes da atualização
        old_image = PerfilUsuario.objects.get(pk=instance.pk).foto_perfil
    except PerfilUsuario.DoesNotExist:
        return

    # Recupera a nova imagem que será salva
    new_image = instance.foto_perfil

    # Se a imagem foi alterada e o arquivo antigo existe, exclua-o
    if old_image and old_image != new_image:
        if old_image.path and os.path.isfile(old_image.path):
            os.remove(old_image.path)
