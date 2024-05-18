from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from . import models
    
    
class UpdatePerfilForm(forms.ModelForm):
    class Meta:
        model = models.PerfilUsuario
        fields = ['nome', 'data_nascimento', 'foto_perfil']

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data['data_nascimento']
        idade = int((date.today() - data_nascimento).days / 365.25)  # Calcula a idade em anos
        if idade < 18:
            raise ValidationError("Você deve ter pelo menos 18 anos para se cadastrar.")
        return data_nascimento