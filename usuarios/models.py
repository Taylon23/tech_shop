from django.db import models
from django.contrib.auth.models import User
from produtos import models as model_produto


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.usuario.username
    
         
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(model_produto.ProdutoModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'produto')

    def __str__(self):
        return f'{self.usuario.username} - {self.produto.titulo}'