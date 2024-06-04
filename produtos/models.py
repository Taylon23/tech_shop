from django.db import models
from . import choices
from django.urls import reverse
from django.utils.http import urlencode


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
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(CategoriasModel, on_delete=models.PROTECT)

    # Informações específicas basica do produto
    marca = models.ForeignKey(MarcasModel, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    sistema_operacional = models.CharField(
        max_length=50, blank=True, null=True)
    tipo_armazenamento = models.CharField(
        max_length=100, blank=True, null=True)
    capacidade_armazenamento = models.CharField(
        max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    memoria_ram_expansivel = models.CharField(
        max_length=50, blank=True, null=True)
    tamanho_tela = models.CharField(max_length=50, blank=True, null=True)
    processador = models.CharField(max_length=100, blank=True, null=True)
    velocidade_processador = models.CharField(
        max_length=50, blank=True, null=True)
    tipo_placa_video = models.CharField(max_length=100, blank=True, null=True)

    # destacar produto
    destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detalhe-produto', args=[self.id])
    
    # API do whatsapp para mandar mensagem do produto para o vendendor
    def whatsapp_url(self, request):
        numero = '98991730451'
        produto_url = request.build_absolute_uri(self.get_absolute_url())
        mensagem = f'Estou interessado no seguinte produto: {produto_url}'
        params = urlencode({'phone': numero, 'text': mensagem})
        return f'https://api.whatsapp.com/send?{params}'

    def __str__(self):
        return self.titulo
