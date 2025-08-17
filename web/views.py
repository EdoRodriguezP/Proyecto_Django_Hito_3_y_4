from django.shortcuts import render, redirect
from .models import Producto, Contactoform
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import Contacto_Formulario 


def home(request):
    productos = Producto.objects.filter(premium=False).prefetch_related('imagenes')

    return render(request, 'web/home.html', {'productos': productos})

@login_required
def premium(request):
    productos = Producto.objects.filter(premium=True).prefetch_related('imagenes')
    return render(request, 'web/premium.html', {'productos': productos})

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'web/detalle_producto.html'
    context_object_name = 'producto'

def contacto(request):
    if request.method == 'POST':
        form = Contacto_Formulario(request.POST)
        if form.is_valid():

            Contacto_form = Contactoform.objects.create(**form.cleaned_data)
            # Aquí podrías guardar el formulario en la base de datos si lo deseas
            # Contactoform.objects.create(**form.cleaned_data)
            return redirect('exito')  # Redirigir a una página de agradecimiento
    else:
        form = Contacto_Formulario()
    
    return render(request, 'web/contacto.html', {'form': form})

def exito(request):
    return render(request, 'web/exito.html')  # Asegúrate de tener una plantilla llamada 'exito.html'