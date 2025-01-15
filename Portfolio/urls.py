from django.urls import path, re_path

from MyPortfolio import settings
from . import views
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
    path('',views.home,name='home'),
    path('portfolio/project/<str:project_name>/',views.projectInfo,name="project"),
    path('download-resume',views.downloadResume,name='download-resume'),
]