from django.contrib import admin
from  . import models


admin.site.register(models.ProdutoModel)
admin.site.register(models.CategoriasModel)
admin.site.register(models.MarcasModel)

