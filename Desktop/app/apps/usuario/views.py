from django.shortcuts import render, redirect
from .forms import CustomCreationForm
from .models import Perfil ,Friend, proveedorRecompensa, recompensa, noticias, Estadistica, Reciclaje
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages, admin

# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    recompensas = []
    for a in proveedor:
        recompensas = recompensa.objects.prefetch_related('idproveedor').filter(activo=True)
    premios = zip(proveedor,recompensas)
    noticia = noticias.objects.all()[:2]
    context ={'premios':premios,'noticia':noticia}
    return render(request,'usuario/menu/Home.html',context)

def Recuperar_contraseña(request):
    return render(request, 'usuario/Ingreso/Recuperar_contraseña.html')

def Account(request):
    user = request.user
    try:
        Puntos = Estadistica.objects.get(idUsuario=user.id)
        Cantidad = Estadistica.get_cantidad(user.id)
        context={'estadistica':Puntos,'cantidad':Cantidad}
        return render(request, 'usuario/Perfil/Perfil.html',context)
    except Estadistica.DoesNotExist:
         return redirect(admin.site.urls)

def Account_amigos(request):
    user = request.user
    try:
        amigos = Friend.objects.prefetch_related('current_user').get(id=user.id)
        for a in amigos:
            last_login = user.last_login
            amigos = zip(amigos,last_login)
        context = {'amigos':amigos}
        return render(request, 'usuario/Perfil/Amigos.html',context)
    except Friend.DoesNotExist:   
        return render(request, 'usuario/Perfil/Amigos.html')

def Account_premios(request):
    proveedor = proveedorRecompensa.objects.all()
    for a in proveedor:
        recompensas = recompensa.objects.prefetch_related('idproveedor').filter(activo=True)
    premios = zip(proveedor,recompensas)
    context = {'premios':premios}
    return render(request, 'usuario/Perfil/Premios.html',context)

def Account_noticias(request):
    noticia = noticias.objects.all()
    context ={'noticia':noticia}
    return render(request, 'usuario/Perfil/Noticias.html',context)

def Account_settings(request):
    user = request.user
    context ={'Usuario':user}
    return render(request, 'usuario/Perfil/Configuracion.html',context)

def Login(request):
    if request.method == 'POST':
        user = Perfil.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('')
        else:
            try:
                user = Perfil.objects.get(username=request.POST['username'])
                if user.password == request.POST['password']:
                    request.session['member_id']=user.id
                    return redirect(Home)
                else:
                    messages.error(request, 'El nombre de usuario y/o contraseña son invalidos', extra_tags='username')
                    return render(request, 'usuario/Ingreso/Login.html')
            except Perfil.DoesNotExist:
                messages.error(request, 'El nombre de usuario y/o contraseña son invalidos', extra_tags='username')
                return render(request, 'usuario/Ingreso/Login.html')
    else:
        return render(request, 'usuario/Ingreso/Login.html')

def Logout(request):
    logout(request)
    return redirect(Home)

def Registrar(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Perfil.authenticate(request, username, password)
            login(request,user)
            return redirect(Home)
        else:
            form = CustomCreationForm()
            return render(request,'usuario/Ingreso/Registro.html',{'form': form})
    else:
        form = CustomCreationForm()
        return render(request,'usuario/Ingreso/Registro.html',{'form': form})
    

        




