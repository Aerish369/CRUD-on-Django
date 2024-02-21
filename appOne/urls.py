from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),

    path('projects/', views.projects, name="projects" ),
    path('view-project/<str:pk>/', views.viewProject, name="view-project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),

    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact" ),
]
