from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import loader
from django.contrib.auth import logout
from .models import Register

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def register(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    phone_number = request.POST.get['phone_number']
    gender = request.POST.get['gender']
    Obj1 = Register(username = username, password = password,phone_number = phone_number, gender = gender)
    Obj1.save()
    return render(request, 'main.html',{'message': 'registered!'})




def Logout(request):
    logout(request)
    
    
def login(request):
    render(request, login.html)