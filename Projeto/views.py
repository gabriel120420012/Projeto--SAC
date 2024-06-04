from django.shortcuts import render, get_object_or_404, redirect
from cpasisApp.models import Eixo, Dimensao, Indicador
from cpasisApp.forms import EixoForm, DimensaoForm, IndicadorForm


# Create your views here.
def principal(request):
    return render(request, 'cpasis/principal.html')


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


#dimensional

def new_dim(request):
    form = DimensaoForm(request.POST)
    dims = Dimensao.objects.all()

    if request.method == 'POST':
        form = DimensaoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form =DimensaoForm()
    context = {'form': form, 'dims': dims}
    return render(request, 'cpasis/new_dimensao.html', context)

        
def deletar_dim(request, id):
    dim = get_object_or_404(Dimensao, pk=id)
    form = DimensaoForm(instance=dim)
    dims = Dimensao.objects.all()
    if (request.method == "POST"):
        dim.delete()
        return redirect('new_dim')
        return render(request, "cpasis/deletar_dimensao.html", {'dim': dim, 'form': form, 'dims': dims})

    else:
        return render(request, "cpasis/editar_dimensao.html", {'form': form, 'dim': dim, 'dims': dims})
    
def editar_dim(request, id):
    dim = get_object_or_404(Dimensao, pk=id)
    form = DimensaoForm(instance=dim)
    dims = Dimensao.objects.all()

    if (request.method == "POST"):
        form = DimensaoForm(request.POST, request.FILES, instance=dim)

        if form.is_valid():
            form.save()
            return redirect('new_dim')

        else:

            return render(request, "cpasis/editar_dimensao.html", {'dim': form, 'form': dim, 'dims': dims})
    else:
        return render(request, "cpasis/editar_dimensao.html", {'form': form, 'dim': dim, 'dims': dims})
    

# novo indicador

def editar_indicador(request,id):
    indicador = get_object_or_404(Indicador, pk=id)
    form = IndicadorForm(instance=indicador)
    indicadores = Indicador.objects.all()

    if (request.method == "POST"):
        form = IndicadorForm(request.POST, request.FILES, instance=indicador)

        if form.is_valid():
            form.save()
            return redirect('new_indicador')
        
        else:
            return render(request, "cpasis/editar_indicador.html", {'form': form, 'indicador': indicador, 'indicadores': indicadores})

    else: 
        return render(request, "cpasis/editar_indicador.html", {'form': form, 'indicador': indicador, 'indicadores': indicadores})    


# new inde
def new_inde(request):
    form = IndicadorForm(request.POST)
    indicadores = Indicador.objects.all()

    if request.method == 'POST':
        form = IndicadorForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            form= IndicadorForm()

    context = {'form': form, 'indicadores': indicadores}  
    return render (request, 'cpasis/new_inde.html', context)      

def deletar_indicador(request, id):
    indicador = get_object_or_404(Indicador, pk=id)
    form = IndicadorForm(instance=indicador)
    indicadores = Indicador.objects.all()
    
    if (request.method =='POST'):
        indicador.delete()
        return redirect('deletar_indicador')

        return render(request,"cpasis/deletar_indicador", {'indicador': indicador, 'form': form, 'indicadores': indicadores})   

    else: 

        return render(request, "cpasis/editar_indicador.html", {'form': form, 'indicador': indicador, 'indicadores': indicadores})