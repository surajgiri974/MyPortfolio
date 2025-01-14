from pathlib import Path
from django.shortcuts import render

from Portfolio.models import Project,ProjectImage


def home(request):
    try:
        project = Project.objects.all()
        return render(request,"index.html",{'project':project})
    except:
        return render(request,'index.html')


def projectInfo(request,project_name):
    try:
        project_info = Project.objects.get(project_name = project_name)
        project_images = ProjectImage.objects.filter(project = project_info)
        print(project_images)
        return render(request,"developed-details.html",{'project_info':project_info,'project_images':project_images})
    except:
        return render(request,'developed-details.html')
    