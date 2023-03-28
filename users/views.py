from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm #Eliminado al cargar #from .forms import UserRegisterForm (Linea 4)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #Cambiado de UserCreationForm() a UserRegisterForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm() #Cambiado de UserCreationForm() a UserRegisterForm
    return render(request, 'users/register.html', {'form':form} )

@login_required
def profile(request):
    return render(request,'users/profile.html')
