from django.urls import path,include
from rest_framework import routers
from user_app.views import login_view,set_password_view,ProjectViewSet,CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'projects',ProjectViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',login_view,name='login'),
    path('set-password/',set_password_view,name='set-password'),
]