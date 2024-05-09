from django.shortcuts import render,get_object_or_404
from . import models


def detalhe_produto(request,id):
    produto = get_object_or_404(models.ProdutoModel,id=id)  
    return render(request,'detalhes_produto.html',{'produto':produto})
