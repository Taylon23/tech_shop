from . import models

def favoritos_do_usuario(request):
    favoritos = []
    if request.user.is_authenticated:
        favoritos = models.Favorito.objects.filter(usuario=request.user).values_list('produto_id', flat=True)
    return {'favoritos_do_usuario': favoritos}
