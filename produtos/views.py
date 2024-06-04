from django.shortcuts import render, get_object_or_404
from . import models


def detalhe_produto(request, id):
    produto = get_object_or_404(models.ProdutoModel, id=id)
    whatsapp_url = produto.whatsapp_url(request)
    return render(request, 'detalhes_produto.html', {'produto': produto, 'whatsapp_url': whatsapp_url})
