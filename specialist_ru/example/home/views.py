from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from django.utils.http import is_safe_url, urlunquote
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForms

def home_page(request):
    local_time = datetime.now()

    context = {

        'local_time': local_time
    }

    return render(request, 'main.html', context)


def login_user(request):
    #Авторизация (вход в систему)
    form = LoginForms(request.POST)

    if form.is_valid():
        alogin = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(request, username=alogin, password=password)

        if user is not None:
            login(request, user)

    way = request.META.get('HTTP_REFERER')
    if way:
        way = urlunquote(way)
        print('login')

    if not is_safe_url(url=way, allowed_hosts=request.get_host()):
        way = reverse('home:index')
    
    return HttpResponseRedirect(way)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))