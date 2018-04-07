from django.urls import path

from . import views

urlpatterns = [
    #url to the
    path('', views.index, name='index' ),
]
