from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Venda
from .forms import VendaForm


# Dashboard
def inicio(request):
    vendas = Venda.objects.filter(
        data__lte=timezone.now()).order_by('data')[:10]
    return render(request, 'venda/index.html', {'vendas': vendas})


# Histórico
def historico(request):
    vendas = Venda.objects.filter(data__lte=timezone.now()).order_by('data')

    pesquisa = request.GET.get('q')
    if pesquisa:
        vendas = vendas.filter(
            Q(id__icontains=pesquisa) |
            Q(data__icontains=pesquisa) |
            Q(descricao__icontains=pesquisa)
        )

    return render(request, 'venda/historico.html', {'vendas': vendas})


# Adicionar
def adicionar(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('historico')

    return render(request, 'venda/adicionar.html', {'form': form})


# Atualizar
def atualizar(request, id):
    venda = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=venda)

    if form.is_valid():
        form.save()
        return redirect('historico')

    return render(request, 'venda/adicionar.html', {'form': form, 'venda': venda})


# Deletar
def deletar(request, id):
    venda = Venda.objects.get(id=id)
    venda.delete()
    return redirect('historico')
