from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


from .forms import RegisterForm , Contacto_Form
from django.contrib.auth.models import User
from .models import Contacto #, ContactoForm
# Create your views here.

def index(request):
    return render(request,'index.html', {

    })
def ingresar(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request,'Inicio_sesion.html', {

    })

    
def nosotros(request):
    return render(request,'Quienes_somos.html', {

    })
def registro(request):
    return render(request,'Registro.html', {

    })
def salir_sistema(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('ingresar')
def registroU(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')#Diccionario
        email = form.cleaned_data.get('email')#Diccionario
        password = form.cleaned_data.get('password')#Diccionario
        user = User.objects.create_user(username, email, password) #metodo create user 
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    return render(request, 'registro.html', {'form': form})

def add_contacto(request):
    if request.method == "POST":
        form = Contacto_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = Contacto_Form()
    return render(request, 'contacto.html', {'form': form})


