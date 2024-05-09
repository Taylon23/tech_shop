from django.shortcuts import render
from produtos import models as produtomodel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    produtos = produtomodel.ProdutoModel.objects.filter(destaque=True)
    return render(request,'home.html',{'produtos':produtos})

def search(request):
    query = request.GET.get('q')  # Obtém a consulta de pesquisa do parâmetro GET 'q'
    
    if query:  # Se houver uma consulta de pesquisa
        produtos = produtomodel.ProdutoModel.objects.filter(titulo__icontains=query)  # Filtra os produtos com base no título contendo a consulta
    else:
        produtos = []  # Se não houver consulta de pesquisa, retorna uma lista vazia
    
    return render(request, 'search.html', {'produtos': produtos, 'query': query})
