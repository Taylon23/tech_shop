from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
import os
from . import models


@receiver(post_delete, sender=models.ProdutoModel)
def delete_produto_imagem(sender, instance, **kwargs):
    # Verifica se existe uma imagem associada ao ProdutoModel
    if instance.imagem:
        # Exclui a imagem do sistema de arquivos
        if os.path.isfile(instance.imagem.path):
            os.remove(instance.imagem.path)
            

@receiver(pre_save, sender=models.ProdutoModel)
def update_produto_imagem(sender, instance, **kwargs):
    if instance.pk:  # Verifica se o objeto já existe no banco de dados (ou seja, se está sendo atualizado)
        try:
            # Obtém o objeto existente no banco de dados
            produto = models.ProdutoModel.objects.get(pk=instance.pk)
        except models.ProdutoModel.DoesNotExist:
            return

        if produto.imagem != instance.imagem:
            # Se a imagem do produto existente for diferente da nova imagem,
            # exclui a imagem antiga do sistema de arquivos
            if os.path.isfile(produto.imagem.path):
                os.remove(produto.imagem.path)