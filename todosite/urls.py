"""todosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #####################home_page###########################################
    path('',views.index,name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<int:item_id>',views.remove,name="del"),
    ####################give id no. item_id name or item_id=i.id ############
    path('update/',views.update,name="update"),
    ########################################################################
    path('admin/', admin.site.urls),
    ########################################################################
    path('userlogin/', views.login, name="userlogin"),
    ########################################################################
    path('logout/', views.logout, name="logout"),
    ########################################################################
    path('signup/', views.signup, name="signup"),
    ########################################################################
    path('category/', views.category, name="category"),
    ########################################################################
    path('', include('todo.urls')),
]