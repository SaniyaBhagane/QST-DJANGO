from django.urls import path
from Testapp import views

urlpatterns = [
    path('hello/',views.template_view),
    path('about/',views.about),
]