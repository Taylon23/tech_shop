from . import models
from . import choices


def get_first_name(choices):
    # Retorna uma lista com apenas o primeiro nome de cada opção
    return [choice[0] for choice in choices]


def categorias_produtos(request):
    categorias = models.CategoriasModel.objects.exclude(categorias="Notebook")
    marca_notebook = get_first_name(choices.MARCANOTEBOOK_CHOICES) 
    return {'categorias_produtos':categorias,'marca_notebook':marca_notebook}