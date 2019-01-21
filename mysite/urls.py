"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from login import views
import login
import 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login), # 登录页面路由
    path('login_action/', views.login_action), # 登录处理页面路由
    path('registration/', views.registration), # 注册页面路由
    path('sign/', views.sign), # 注册处理路由
    path('index/', views.index), # 首页页面路由

]
handler404 = "login.views.page_not_found"
handler400 = "login.views.bad_request"
handler500 = "login.views.server_error"
