from django.shortcuts import render, redirect, get_object_or_404
from .models import Requerimiento, Categorias

def categorias(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        if nombre:  # Evita guardar vacíos
            Categorias.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('categorias')

    partes = Categorias.objects.all().order_by('nombre')
    return render(request, 'sntd/categorias.html', {'partes': partes})

def eliminar_categoria(request, id):
    parte = Categorias.objects.get(id=id)
    parte.delete()
    return redirect('categorias')

def tablero(request):
    categorias = Categorias.objects.prefetch_related('requerimientos').all()
    return render(request, 'sntd/tablero.html', {'categorias': categorias})

def primera_formula(S, N, T, D):
    return (S+N)*(T+D)

def segunda_formula(S, N, T, D):
    return (S+N)/(T+D)

def home(request):
    return render(request, "sntd/base.html")

def registrar(request):
    categorias = Categorias.objects.all().order_by('nombre')

    if request.method == "POST":
        id_rf = request.POST.get("id_rf")
        nombre_form = request.POST.get("name_rf")  # <-- así se llama en el HTML
        S = int(request.POST.get("satisfaccion"))
        N = int(request.POST.get("necesidad"))
        T = int(request.POST.get("tecnica"))
        D = int(request.POST.get("dependencia"))
        opcion = int(request.POST.get("opcion"))
        categoria_id = request.POST.get("categoria")

        if opcion == 1:
            resultado = primera_formula(S, N, T, D)
        else:
            resultado = segunda_formula(S, N, T, D)

        categoria = Categorias.objects.get(id=categoria_id) if categoria_id else None

        # 👇 Aquí se guarda usando el nombre del campo en el modelo
        Requerimiento.objects.create(
            id_rf=id_rf,
            nombre=nombre_form,      # ✅ el modelo tiene 'nombre'
            categoria=categoria,
            satisfaccion=S,
            necesidad=N,
            tecnica=T,
            dependencia=D,
            resultado=resultado,
        )

        return redirect("listar")

    return render(request, "sntd/registrar.html", {"categorias": categorias})


def listar(request):
    requerimientos = Requerimiento.objects.all().order_by("-resultado")
    return render(request, "sntd/listar.html", {"requerimientos": requerimientos})


def completar(request, id):
    req = get_object_or_404(Requerimiento, id=id)
    req.completado = True
    req.save()
    return redirect("listar")


def eliminar(request, id):
    req = get_object_or_404(Requerimiento, id=id)
    req.delete()
    return redirect("listar")
