from django.urls import path
from testApp import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('persons/add/', views.add_person, name='add_person'),

    path('aadhar/', views.aadhar_list, name='aadhar_list'),
    path('aadhar/add/', views.add_aadhar, name='add_aadhar'),

    path('fathers/', views.father_list, name='father_list'),
    path('fathers/add/', views.add_father, name='add_father'),

    path('children/', views.children_list, name='children_list'),
    path('children/add/', views.add_child, name='add_child'),
]
