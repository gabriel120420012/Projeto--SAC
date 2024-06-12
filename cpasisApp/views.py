from django.shortcuts import render, get_object_or_404, redirect
from cpasisApp.models import Eixo, Dimensao, Indicador, Campus, Publico, Curso, TipoCurso
from cpasisApp.forms import EixoForm, DimensaoForm, IndicadorForm,TipoForm, CursoForm,PublicoForm,CampusForm


# Create your views here.
def principal(request):
    return render(request, 'cpasis/principal.html')

def index(request):
    return render(request, 'cpasis/index.html')

def login(request):
    return render(request, 'cpasis/login.html')

def register(request):
    return render(request, 'cpasis/register.html')

def index1(request):
    return render(request, 'cpasis/index1.html')

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


# Dimensão
def new_dim(request):
    form = DimensaoForm(request.POST)
    dims = Dimensao.objects.all()

    if request.method == 'POST':
        form = DimensaoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = DimensaoForm()
    context = {'form': form, 'dims': dims}
    return render(request, 'cpasis/new_dim.html', context)


def editar_dim(request, id):
    dim = get_object_or_404(Dimensao, pk=id)
    form =DimensaoForm(instance=dim)
    dims = Dimensao.objects.all()

    if (request.method == "POST"):
        form = DimensaoForm(request.POST, request.FILES, instance=dim)

        if form.is_valid():
            form.save()
            return redirect('new_dim')

        else:

            return render(request, "cpasis/editar_dim.html", {'form': form, 'dim': dim, 'dims': dims})
    else:
        return render(request, "cpasis/editar_dim.html", {'form': form, 'dim': dim, 'dims': dims})


def deletar_dim(request, id):
    dim = get_object_or_404(Dimensao, pk=id)
    form = DimensaoForm(instance=dim)
    dims = Dimensao.objects.all()
    if (request.method == "POST"):
        dim.delete()
        return redirect('new_dim')
    return render(request, "cpasis/deletar_dim.html", {'dim': dim, 'form': form, 'dims': dims})


# indicadores
def new_ind(request):
    form = IndicadorForm(request.POST)
    inds = Indicador.objects.all()

    if request.method == 'POST':
        form = IndicadorForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = IndicadorForm()
    context = {'form': form, 'inds': inds}
    return render(request, 'cpasis/new_ind.html', context)


def editar_ind(request, id):
    ind = get_object_or_404(Indicador, pk=id)
    form =IndicadorForm(instance=ind)
    inds = Indicador.objects.all()

    if (request.method == "POST"):
        form = IndicadorForm(request.POST, request.FILES, instance=ind)

        if form.is_valid():
            form.save()
            return redirect('new_ind')

        else:

            return render(request, "cpasis/editar_ind.html", {'form': form, 'ind': ind, 'inds': inds})
    else:
        return render(request, "cpasis/editar_ind.html", {'form': form, 'ind': ind, 'inds': inds})


def deletar_ind(request, id):
    ind = get_object_or_404(Indicador, pk=id)
    form = IndicadorForm(instance=ind)
    inds = Indicador.objects.all()
    if (request.method == "POST"):
        ind.delete()
        return redirect('new_ind')
    return render(request, "cpasis/deletar_ind.html", {'ind': ind, 'form': form, 'inds': inds})

# campus
def new_campus(request):
    form = CampusForm(request.POST)
    campi = Campus.objects.all()

    if request.method == 'POST':
        form = CampusForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = CampusForm()
    context = {'form': form, 'campi': campi}
    return render(request, 'cpasis/new_campus.html', context)


def editar_campus(request, id):
    campus = get_object_or_404(Campus, pk=id)
    form =CampusForm(instance=campus)
    campi = Campus.objects.all()

    if (request.method == "POST"):
        form = CampusForm(request.POST, request.FILES, instance=campus)

        if form.is_valid():
            form.save()
            return redirect('new_campus')

        else:

            return render(request, "cpasis/editar_campus.html", {'form': form, 'campus': campus, 'campi': campi})
    else:
        return render(request, "cpasis/editar_campus.html", {'form': form, 'campus': campus, 'campi': campi})


def deletar_campus(request, id):
    campus = get_object_or_404(Campus, pk=id)
    form = CampusForm(instance=campus)
    campi = Campus.objects.all()
    if (request.method == "POST"):
        campus.delete()
        return redirect('new_campus')
    return render(request, "cpasis/deletar_campus.html", {'campus': campus, 'form': form, 'campi': campi})

#publico
def new_pub(request):
    form = PublicoForm(request.POST)
    pubs = Publico.objects.all()

    if request.method == 'POST':
        form = PublicoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = PublicoForm()
    context = {'form': form, 'pubs': pubs}
    return render(request, 'cpasis/new_publico.html', context)


def editar_publico(request, id):
    pub = get_object_or_404(Publico, pk=id)
    form =PublicoForm(instance=pub)
    pubs = Publico.objects.all()

    if (request.method == "POST"):
        form = PublicoForm(request.POST, request.FILES, instance=pub)

        if form.is_valid():
            form.save()
            return redirect('new_pub')

        else:

            return render(request, "cpasis/editar_publico.html", {'form': form, 'pub': pub, 'pubs': pubs})
    else:
        return render(request, "cpasis/editar_publico.html", {'form': form, 'pub': pub, 'pubs': pubs})




def deletar_publico(request, id):
    pub = get_object_or_404(Publico, pk=id)
    form =PublicoForm(instance=pub)
    pubs = Publico.objects.all()
    if (request.method == "POST"):
        pubs.delete()
        return redirect('new_pub')
    return render(request, "cpasis/deletar_publico.html", {'pub': pub, 'form': form, 'pubs': pubs})

#tipo curso

def new_tipo(request):
    form = TipoForm(request.POST)
    tipos = TipoCurso.objects.all()

    if request.method == 'POST':
        form = TipoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = TipoForm()
    context = {'form': form, 'tipos': tipos}
    return render(request, 'cpasis/new_tipo.html', context)


def editar_tipo(request, id):
    tipo = get_object_or_404(TipoCurso, pk=id)
    form =TipoForm(instance=tipo)
    tipos = TipoCurso.objects.all()

    if (request.method == "POST"):
        form = TipoForm(request.POST, request.FILES, instance=tipos)

        if form.is_valid():
            form.save()
            return redirect('new_tipo')

        else:

            return render(request, "cpasis/editar_tipo.html", {'form': form, 'tipo': tipo, 'tipos': tipos})
    else:
        return render(request, "cpasis/editar_tipo.html", {'form': form, 'tipo': tipo, 'tipos': tipos})




def deletar_tipo(request, id):
    tipo = get_object_or_404(TipoCurso, pk=id)
    form =TipoForm(instance=tipo)
    tipos = TipoCurso.objects.all()
    if (request.method == "POST"):
        tipos.delete()
        return redirect('new_pub')
    return render(request, "cpasis/deletar_tipo.html", {'tipo': tipo, 'form': form, 'tipos': tipos})


# curso

def new_curso(request):
    form = CursoForm(request.POST)
    cursos = Curso.objects.all()

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = CursoForm()
    context = {'form': form, 'cursos': cursos}
    return render(request, 'cpasis/new_curso.html', context)


def editar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    form =CursoForm(instance=curso)
    cursos = Curso.objects.all()

    if (request.method == "POST"):
        form = CursoForm(request.POST, request.FILES, instance=cursos)

        if form.is_valid():
            form.save()
            return redirect('new_curso')

        else:

            return render(request, "cpasis/editar_curso.html", {'form': form, 'curso':curso , 'cursos': cursos})
    else:
        return render(request, "cpasis/editar_curso.html", {'form': form, 'curso': curso, 'cursos': cursos})




def deletar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    form =CursoForm(instance=curso)
    cursos = Curso.objects.all()
    if (request.method == "POST"):
        cursos.delete()
        return redirect('new_pub')
    return render(request, "cpasis/deletar_curso.html", {'curso': curso, 'form': form, 'cursos': cursos})

