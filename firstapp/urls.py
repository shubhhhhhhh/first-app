"""
URL configuration for firstapp project.

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
from django.urls import path,include
#from products import views
from account_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # setting path for different apps by defining their urls here
    #  path('products/',views.first),
    path('signup/',views.account_signup),
    path('success/',views.success),
    path('home/',views.home),
    path('',views.new_account),
    path('employee/',views.getEmployee),
    path('login/',views.login),
    path('loginpage/',views.Login_Page),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls'))
]
