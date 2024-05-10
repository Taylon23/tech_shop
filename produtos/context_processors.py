from . import models

def categorias_produtos(request):
    categoria = models.CategoriasModel.objects.all()
    marca_notebook = models.MarcasModel.objects.all()
    return {'categorias_produtos':categoria,'marca_notebook':marca_notebook}