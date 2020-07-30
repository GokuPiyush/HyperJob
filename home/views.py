from django.shortcuts import render
from django.views import View
from django.core.exceptions import PermissionDenied

# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {'create': 'none'}
        if request.user.is_authenticated:
            if request.user.is_staff:
                context['create'] = 'vacancy'
            else:
                context['create'] = 'resume'
        return render(request, 'home/index.html', context=context)
    def post(self, request):
        raise PermissionDenied()
