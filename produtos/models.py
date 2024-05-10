from django.db import models



class CategoriasModel(models.Model):
    categorias = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categorias
    

class MarcasModel(models.Model):
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.marca
    
class ProdutoModel(models.Model):
    imagem = models.ImageField(upload_to='produto')
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=6)
    descricao = models.TextField()
    marca = models.ForeignKey(MarcasModel,on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(CategoriasModel,on_delete=models.PROTECT)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
