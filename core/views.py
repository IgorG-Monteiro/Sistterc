from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import TerceirizadoForm
from .models import Terceirizado
import datetime
import pandas as pd
from .gerapdf import gerar_pdf

# Create your views here.
@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

@login_required
def iniciar(request):
    if request.user.is_superuser:
        terc = Terceirizado.objects.filter(is_active = True)
    else:
        terc = Terceirizado.objects.filter(usuario_cadastro = request.user.username).filter(is_active = True)

    current_user = request.user
    context = {}
    context['user'] = current_user
    context['terc'] = terc
    return render(request, 'start.html', context)

@login_required
def cadastrar(request):
    if request.method == 'GET':
        form = TerceirizadoForm()
        current_user = request.user
        context = {}
        context['user'] = current_user
        context['form'] = form
        return render(request, 'cadastrar.html', context)
    else:
        form = TerceirizadoForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Terceirizado.objects.last()
            obj.usuario_cadastro = request.user.username
            obj.save()
            return HttpResponseRedirect('/')
        else:
            form = TerceirizadoForm()
            current_user = request.user
            erro = 'ERRO: Vigência deve estar no formato dd/mm/aaaa'
            context = {}
            context['user'] = current_user
            context['form'] = form
            context['erro'] = erro
            return render(request, 'cadastrar.html', context)

@login_required
def deletar(request, id):
    ativar = Terceirizado.objects.filter(id=id)[0]
    ativar.is_active = False
    ativar.save()
    return HttpResponseRedirect('/')

@login_required
def editar(request, id):
    if request.method == 'GET':
        terc = Terceirizado.objects.filter(id=id)
        form = TerceirizadoForm(instance=terc.first())
        current_user = request.user
        context = {}
        context['user'] = current_user
        context['form'] = form
        context['terc'] = terc
        return render(request, 'editar.html', context)
    else:
        terc = Terceirizado.objects.filter(id=id)
        form = TerceirizadoForm(request.POST, instance=terc.first())
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            terc = Terceirizado.objects.filter(id=id)
            form = TerceirizadoForm(instance=terc.first())
            current_user = request.user
            context = {}
            context['user'] = current_user
            context['form'] = form
            context['terc'] = terc
            return render(request, 'editar.html', context)

@login_required
def gerador(request):
    if request.method == 'GET':
        current_user = request.user

        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        referencia = last_month.strftime("%m/%Y")

        if request.user.is_superuser:
            terc = Terceirizado.objects.filter(is_active = True)
        else:
            terc = Terceirizado.objects.filter(usuario_cadastro = request.user.username).filter(is_active = True)

        context = {}
        context['user'] = current_user
        context['referencia'] = referencia
        context['terc'] = terc

        return render(request, 'gerador_DAES.html', context)


@login_required
def gerador_transparencia(request):
    terc = Terceirizado.objects.filter(is_active = True)
    gerar_todos = terc.all()
    dataframe = pd.DataFrame.from_records(gerar_todos.values())
    gerar_pdf(dataframe)
    

    return HttpResponseRedirect('uploads/transparencia.zip')

def handler404(request, exception):
    return render(request, 'error.html')

def base(request):
    current_user = request.user
    context = {}
    context['user'] = current_user
    return render(request, 'base.html', context)

def start(request):
    if request.user.is_superuser:
        terc = Terceirizado.objects.filter(is_active = True)
    else:
        terc = Terceirizado.objects.filter(usuario_cadastro = request.user.username).filter(is_active = True)

    current_user = request.user
    context = {}
    context['user'] = current_user
    context['terc'] = terc
    return render(request, 'start.html', context)
