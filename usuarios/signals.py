from django.db.models.signals import pre_save
from django.dispatch import receiver
from models import PerfilUsuario
import os


@receiver(pre_save, sender=PerfilUsuario)
def update_perfil_imagem(sender, instance, **kwargs):
    if instance.pk:  # Verifica se o objeto já existe no banco de dados (ou seja, se está sendo atualizado)
        try:
            # Obtém o objeto existente no banco de dados
            perfil = PerfilUsuario.objects.get(pk=instance.pk)
        except PerfilUsuario.DoesNotExist:
            return

        if perfil.foto_perfil and perfil.foto_perfil != instance.foto_perfil:
            # Se a imagem do perfil existente for diferente da nova imagem,
            # exclui a imagem antiga do sistema de arquivos
            if os.path.isfile(perfil.foto_perfil.path):
                os.remove(perfil.foto_perfil.path)