from django.urls import path

from . import views

urlpatterns = [
    #url to the
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('executive/', views.admin, name='executive'),
    path('applicant/', views.admin, name='applicant'),
]
