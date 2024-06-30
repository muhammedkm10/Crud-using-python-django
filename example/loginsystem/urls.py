from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('signup/',views.signup,name='user_signup'),
    path('userlogin/',views.login,name='login'),
    path('admin_login/',views.admin_login,name='admin_login'),
]