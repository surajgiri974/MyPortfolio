from pathlib import Path
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from Portfolio.models import Project,ProjectImage


def home(request):
    try:
        project = Project.objects.all()
        print(project[0].images.url)
        return render(request,"index.html",{'project':project})
    except:
        return render(request,'index.html')


def projectInfo(request,project_name):
    try:
        project_info = Project.objects.get(project_name = project_name)
        project_images = ProjectImage.objects.filter(project = project_info)
        return render(request,"developed-details.html",{'project_info':project_info,'project_images':project_images})
    except:
        return render(request,'developed-details.html')

def downloadResume(request):
    try:
        import os
        from MyPortfolio import settings
        file_path = os.path.join(settings.MEDIA_ROOT,"Resume.pdf")
        if not os.path.exists(file_path):
            raise Http404("File Not Found")
        response = FileResponse(open(file_path,'rb'),content_type="application/pdf")
        response['Content-Disposition'] = f'attachment; filename="Suraj_Giri_Resume" '
        return response
    except:
        raise Http404("File Not Found")
        