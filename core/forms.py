from django.forms import ModelForm
from core.models import Terceirizado

class TerceirizadoForm(ModelForm):
    class Meta:
        model = Terceirizado
        fields = ['nome_completo', 'unidade', 'contrato', 'vigencia', 'contratada', 'cnpj_contratada']

