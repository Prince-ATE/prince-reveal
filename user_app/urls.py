from django.urls import path
from user_app.views import login_view,set_password_view

urlpatterns = [
    path('login/',login_view,name='login'),
    path('set-password/',set_password_view,name='set-password'),
]