from django.urls import path

from . import views

app_name = '1'
urlpatterns = [
    path('', views.w, name='1'),
    path('about/', views.q, name='2')

]
