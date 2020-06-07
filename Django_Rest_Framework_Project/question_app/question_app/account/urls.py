from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    # path('', include(router.urls)),
    path('signup/POST', views.signup,name="signup"),
    path('login', obtain_auth_token,name="login"),
    path('users/GET', views.users,name="users"),
]