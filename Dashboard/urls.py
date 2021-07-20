"""Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, include
from account import views

extra_urlpatterns = [
    path('', views.home),
    path('api/', views.apiOverview, name="api-overview"),
    path('api/task-detail/<str:pk>/', views.taskDetail),
    path('api/task-list/', views.taskList, name="task-list"),
    path('api/task-create/', views.taskCreate, name="task-create"),
    path('api/task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('api/task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(extra_urlpatterns)),


]
