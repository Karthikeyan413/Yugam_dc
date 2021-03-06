from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect

from django.contrib import admin

from ev_wo.forms import RegisterForm
# Create your views here.

@csrf_protect
def register_user(request):
    if(request.user.is_authenticated):
        logout(request)
    registered = False
    if request.method == 'POST':
        form_register = RegisterForm(data=request.POST)

        if form_register.is_valid() :
            user = form_register.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(form_register.errors)
    else:
        form_register = RegisterForm()
    if(registered):
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'registration.html', {
                                                'form_register': form_register,
                                                 })
@csrf_protect
def user_login(request):
    if(request.user.is_authenticated):
        logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user = authenticate(username=username, password=password)

        if user:
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect('/event-admin')

            else:
                return HttpResponse("Account Not Active")
        else:
            # print("u={}p={}".format(username, password))
            return render(request, 'login.html', {'invaliduser': True})
    else:
        return render(request, 'login.html', {})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def event_admin(request):
    return render(request, 'event-admin.html')
def home(request):
    return render(request, 'home.html')