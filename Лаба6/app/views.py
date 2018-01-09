from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View,ListView
from .models import *
from app.registration import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'main.html')


def tickets(request):
    return render(request, 'tickets.html')

def hello(request):
    return render(request, 'hello.html')

def loginn(request):
    return render(request, 'user.html', locals())



def concerts(request, id):
    name = ['BMTH_info', 'CTE_info']
    BMTH_info = 'BMTH bla bla'
    CTE_info = 'Crown the empire bla bla'
    info = [BMTH_info, CTE_info]
    data1 = {'concert': {'id': id}}
    data2 = {'concerts': [{'id': '1', 'concert_name': 'Bring Me The Horizon', 'info': BMTH_info},
                       {'id': '2', 'concert_name': 'Crown The Empire', 'info': CTE_info}]}
    return render(request, 'concerts.html', locals())

class TicketsView(View):
    def get(self, request):
        #variable = 'Django'
        today_date = datetime.now()
        data = {
            'tickets': [
                {'title': 'Первый билет', 'id': 1},
                {'title': 'Второй билет', 'id': 2}
            ]
        }
        return render(request, 'tickets.html', locals())


class TicketView(View):
    def get(self, request, id):
        #variable = 'Django'
        today_date = datetime.now()
        data = {
            'ticket': {
                'id': id
            }
        }
        return render(request, 'ticket.html', locals())

class OrdersView(ListView):
    model = Order
    template_name = 'orders.html'

def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/login/')
    return render(request, 'registration2.html', {'form': form})

def authorization(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Пользователь не найден"
    return render(request, 'auth.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')