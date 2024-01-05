from django.contrib import admin
from django.urls import path, include
from . import views as a_user
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView






urlpatterns = [  
    # path('', a_user.auth_user_index,name='aut_index'),
    # path('term/', a_user.Terms_of_use,name='term'),
    # path('privacy/', a_user.Privacy_policy,name='privacy'),
    path('login/', a_user.login_auth_panel,name='aut_login'),
    path('logout/', a_user.logout_auth_panel,name='auth_logout'),
    path('signup/', a_user.signup_auth_panel,name='aut_signup'),
    # path('home_socail/', a_user.home_socail,name='home_socail'),
    path('signup_stor/', a_user.user_index_panel,name='signup_stor'),
    path("email_verification/<str:id>", a_user.email_verify,name='email_verify'),
    
    # path('forgotpass/', a_user.forgot_pass,name='forgotpass'),
    
    
    
    
    
    
    
]