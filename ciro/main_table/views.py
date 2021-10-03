from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm, CreateNumberForm
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .calleditor import newSIP
from .models import Posts


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')


# def registerPage(request):
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#
#     context = {'form': form}
#     return render(request, 'register.html', context)


def loginPage(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Disabled')
            else:
                messages.info(request, 'Invalid login')
    context = {'form': form}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def createNumber(request):
    error = ''
    form = CreateNumberForm()
    if request.method == 'POST':
        form = CreateNumberForm(request.POST)
        if form.is_valid():
            newSIP(request.POST['callerid'])
            form.save()
            return redirect('home')
        else:
            error = 'Что-то пошло не так. Возможно такой номер уже существует или данные введены неверно'
            return render(request, 'create.html', {'error': error})
    if request.user.is_authenticated:
        context = {'form': form, 'error': error}
        return render(request, 'create.html', context)
    return redirect('login')


def editNumber(request):
    numbers = Posts.objects.all()
    context = {'numbers': numbers}
    return render(request, 'edit-table.html', context)


class NumberUpdateView(UpdateView):
    model = Posts
    template_name = 'editor.html'

    form_class = CreateNumberForm
