"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('create_html_form/', views.create_html_form, name='create_html_form'), 
    path('create_django_form/', views.create_django_form, name='create_django_form'),
    path('create_model_form/', views.create_model_form, name='create_model_form'),

    path('student_detail/<int:id>/', views.student_detail, name='student_detail'),
    path('student_list/', views.student_list, name='student_list'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)