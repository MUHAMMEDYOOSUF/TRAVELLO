from django.urls import path

from travelloapp import views

urlpatterns = [
    path('',views.index,name='index')
]