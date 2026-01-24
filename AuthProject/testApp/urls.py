from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('python/', views.python_test, name='python'),
    path('java/', views.java_test, name='java'),
    path('eyc/', views.eyc_test, name='eyc'),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
]
