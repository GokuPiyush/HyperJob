from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import PermissionDenied
from .models import Resume

# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/index.html', context={'resumes': resumes})
    def post(self, request):
        if request.user.is_authenticated:
            description = request.POST['description']
            if request.user.is_staff:
                raise PermissionDenied()
            else:
                Resume.objects.create(description=description, author=request.user)
                return redirect('/home/')
        else:
            raise PermissionDenied()
