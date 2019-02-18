from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # log in success leads to this page
    path('loginSuccess/', views.loginSuccess, name='loginSuccess')

]