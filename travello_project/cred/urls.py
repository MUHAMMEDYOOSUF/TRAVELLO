from django.urls import path

from cred import views

urlpatterns = [
    path('register',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),


    ]