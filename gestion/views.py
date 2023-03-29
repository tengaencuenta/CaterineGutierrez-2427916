from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto={}
    return render(request,'inicio.html', contexto)

def productos(request):
    productos=[' lenovo',' galaxiA35','tablet','lg']
    contexto={ 'listado':productos}
    return render(request,'list_productos.html', contexto)


def inicio(request):
    contexto={}
    return render(request,'inicio.html', contexto)

def categorias(request):
    productos=['Portatil lenovo','Iphone galaxiA35','Rolex titan','Motog7']
    contexto={ 'listado':categorias}
    return render(request,'list_productos.html', contexto)