from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('home', views.home, name='home'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),
    path('support_staff_dashboard', views.support_staff_dashboard, name='support_staff_dashboard'),
]