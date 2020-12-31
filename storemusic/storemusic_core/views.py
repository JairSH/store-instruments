from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login ,authenticate

# Create your views here.

def home(request):
    return render(request,'storemusic_core/home.html')

def registro_usuario(request):
    data = {
        'form' : CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigir al inicio
            username = formulario.changed_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect("home")
    return render(request,'registration/registrar.html',data)

def guitars(request):
    return render(request,'storemusic_core/guitars.html')

def bass(request):
    return render(request,'storemusic_core/bass.html')

def keyboards(request):
    return render(request,'storemusic_core/keyboards.html')

def drums(request):
    return render(request,'storemusic_core/drums.html')

def accordion(request):
    return render(request,'storemusic_core/accordion.html')

def categories(request):
    return render(request,'storemusic_core/categories.html')
    
def ready_to_pick(request):
    return render(request,'storemusic_core/ready_to_pick.html')