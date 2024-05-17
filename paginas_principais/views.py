from django.shortcuts import render
from produtos import models as produtomodel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    produtos = produtomodel.ProdutoModel.objects.filter(destaque=True)
    return render(request,'home.html',{'produtos':produtos})

def search(request):
    query = request.GET.get('q')
    marca_query = request.GET.get('marca')
    categoria_query = request.GET.get('categoria')
    
    produtos = produtomodel.ProdutoModel.objects.all()
    
    if query:
        produtos = produtos.filter(titulo__icontains=query)
    
    if marca_query:
        produtos = produtos.filter(marca__marca__icontains=marca_query,categoria__categorias='Notebook')
    
    if categoria_query:
        produtos = produtos.filter(categoria__categorias__icontains=categoria_query)
    
    return render(request, 'search.html', {'produtos': produtos, 'query': query, 'marca_query': marca_query, 'categoria_query': categoria_query})
