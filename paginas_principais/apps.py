from django.apps import AppConfig


class PaginasPrincipaisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paginas_principais'
    
    def ready(self):
        import usuarios.signals
