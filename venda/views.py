from django.shortcuts import render
from django.utils import timezone
from .models import Venda


def inicio(request):
    return render(request, 'venda/index.html')


def historico(request):
    vendas = Venda.objects.filter(data__lte=timezone.now()).order_by('data')

    pesquisa = request.GET.get('q')
    if pesquisa:
        vendas = vendas.filter(descricao__icontains = pesquisa)

    return render(request, 'venda/historico.html', {'vendas': vendas})
