from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class LogInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = '/'
    template_name = 'login/index.html'
