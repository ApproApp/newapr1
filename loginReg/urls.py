from django.urls import path

from loginReg.views import login, UserSignupView
from . import views

urlpatterns = [
    #url to the
    path('', login,{'template_name': 'loginReg/login.html'},  name='login'),
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('admin/', views.admin, name='admin'),
    path('executive/', views.admin, name='executive'),
    path('applicant/', views.admin, name='applicant'),
]
