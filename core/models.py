from django.db import models
from datetime import datetime

# Create your models here.
class Terceirizado(models.Model):
    nome_completo = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    contrato = models.CharField(max_length=100)
    vigencia = models.DateField()
    contratada = models.CharField(max_length=100)
    cnpj_contratada = models.CharField(max_length=18)
    usuario_cadastro = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def clean(self):
        self.nome_completo = self.nome_completo.title()
        self.unidade = self.unidade.upper()
        self.contratada = self.contratada.upper()
        self.contrato = self.contrato.upper()
        self.cnpj_contratada = self.cnpj_contratada[0:2]+'.'+self.cnpj_contratada[2:5]+'.'+self.cnpj_contratada[5:8]+'/'+self.cnpj_contratada[8:12]+'-'+self.cnpj_contratada[12:14]