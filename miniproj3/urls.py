"""
URL configuration for miniproj3 project.

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
from app1.views import index,about,register,login,contact,doregister,logincheck,action,userhome,adminhome,viewuser,modify
from app2.views import room,aboutus,patient,contactus,actionHCG,view,visited
admin.site.site_header="Oncology_Admin"
#from app2.views import download_pdf,visited

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about',about),
    #path('downloadfile',download_pdf),
   # path('register',register_view,name='register'),
    path('register',register),
    path('login',login),
    path('contact',contact),
    path('userhome',userhome),
    path('adminhome',adminhome),
    path('viewuser/',viewuser),
    path('modify/',modify),
    path('doregister',doregister),
    path('logincheck/',logincheck),
    path('action',action),
    path('',room),
    path('patient/',patient),
    path('visited/',visited),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('actionHCG/',actionHCG),
    path('view/',view),
   # path('visited/<str:filename>/', visited, name='visited'),  # Handle file downloads
  #  path('download_pdf/', download_pdf, name='download_pdf'),
   # path('download_my_pdf', download_pdf, name="download_pdf"),

]

 #   path('downloadfile/', downloadfile, name='downloadfile'),  

