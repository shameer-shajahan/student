"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from studentcrm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_form/',views.StudentView.as_view(),name="student_form"),
    path('student_list/',views.StudentList.as_view(),name="student_list"),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student_detail"),
    path('student/<int:pk>/remove/',views.StudentDeleteView.as_view(),name="student_delete"),
    path('student/<int:pk>/update/',views.StudentUpdateView.as_view(),name="student_update"),
    path('signup/',views.SignupView.as_view(),name="register"),
    path('signin/',views.SigninView.as_view(),name="signin"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 