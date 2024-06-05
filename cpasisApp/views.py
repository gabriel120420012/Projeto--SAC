from django.shortcuts import render, get_object_or_404, redirect
from cpasisApp.models import Eixo, Dimensao, Indicador
from cpasisApp.forms import EixoForm, DimensaoForm, IndicadorForm


# Create your views here.
def principal(request):
    return render(request, 'cpasis/principal.html')

def index(request):
    return render(request, 'cpasis/index.html')

def login(request):
    return render(request, 'cpasis/login.html')

def register(request):
    return render(request, 'cpasis/register.html')

def new_eixo(request):
    form = EixoForm(request.POST)
    eixos = Eixo.objects.all()

    if request.method == 'POST':
        form = EixoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = EixoForm()
    context = {'form': form, 'eixos': eixos}
    return render(request, 'cpasis/new_eixo.html', context)


def editar_eixo(request, id):
    eixo = get_object_or_404(Eixo, pk=id)
    form = EixoForm(instance=eixo)
    eixos = Eixo.objects.all()

    if (request.method == "POST"):
        form = EixoForm(request.POST, request.FILES, instance=eixo)

        if form.is_valid():
            form.save()
            return redirect('new_eixo')

        else:

            return render(request, "cpasis/editar_eixo.html", {'form': form, 'eixo': eixo, 'eixos': eixos})
    else:
        return render(request, "cpasis/editar_eixo.html", {'form': form, 'eixo': eixo, 'eixos': eixos})


def deletar_eixo(request, id):
    eixo = get_object_or_404(Eixo, pk=id)
    form = EixoForm(instance=eixo)
    eixos = Eixo.objects.all()
    if (request.method == "POST"):
        eixo.delete()
        return redirect('new_eixo')
    return render(request, "cpasis/deletar_eixo.html", {'eixo': eixo, 'form': form, 'eixos': eixos})
