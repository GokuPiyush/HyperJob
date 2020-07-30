from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import PermissionDenied
from .models import Vacancy

# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/index.html', context={'vacancies': vacancies})
    def post(self, request):
        if request.user.is_authenticated:
            description = request.POST['description']
            if request.user.is_staff:
                Vacancy.objects.create(description=description, author=request.user)
                return redirect('/home/')
            else:
                raise PermissionDenied()
        raise PermissionDenied()

