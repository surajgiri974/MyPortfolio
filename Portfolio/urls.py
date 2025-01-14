from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('portfolio/project/<str:project_name>/',views.projectInfo,name="project"),
]