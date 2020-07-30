"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import MenuView
from resume.views import ResumeView
from vacancy.views import VacancyView
from signup.views import SignUpView
from login.views import LogInView
from home.views import HomeView
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', MenuView.as_view()),
    path('signup', SignUpView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('login', LogInView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('home', HomeView.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
    path('logout', LogoutView.as_view()),
    path('resumes/', ResumeView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('resume/new', ResumeView.as_view()),
    path('vacancy/new', VacancyView.as_view()),
    path('none/new', HomeView.as_view()),
    path('admin/', admin.site.urls),
]
