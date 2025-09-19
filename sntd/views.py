from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Requerimiento

def primera_formula(S, N, T, D):
    return (S+N)*(T+D)

def segunda_formula(S, N, T, D):
    return (S+N)/(T+D)

def home(request):
    return render(request, "sntd/base.html")

def registrar(request):
    if request.method == "POST":
        id_rf = request.POST["id_rf"]
        S = int(request.POST["satisfaccion"])
        N = int(request.POST["necesidad"])
        T = int(request.POST["tecnica"])
        D = int(request.POST["dependencia"])
        opcion = int(request.POST["opcion"])

        if opcion == 1:
            resultado = primera_formula(S, N, T, D)
        else:
            resultado = segunda_formula(S, N, T, D)

        Requerimiento.objects.create(
            id_rf=id_rf,
            satisfaccion=S,
            necesidad=N,
            tecnica=T,
            dependencia=D,
            resultado=resultado,
        )
        return redirect("listar")

    return render(request, "sntd/registrar.html")


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
