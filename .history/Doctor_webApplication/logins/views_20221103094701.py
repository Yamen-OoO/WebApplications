from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
# Create your views here.
class LoginView(TemplateView):
    template_name = 'templates/login.html'
    
    
    def post(self,request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username = username, password = password)
        if user is not None and user.is_active:
            login(request,user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        