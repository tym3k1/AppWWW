# plik ankiety/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('osoba/', views.osoba_list, name='osoba-list'),
    path('osoba/<int:pk>/', views.RetrieveOsobaView.as_view(), name='retrieve-osoba'),
    path('osoba/<int:pk>/delete/', views.DestroyOsobaView.as_view(), name='destroy-osoba'),
    path('osoba-list-filter/', views.osoba_list_filter, name='osoba-list-filter'),
    path('osoba/<int:pk>/', views.osoba_detail, name='osoba-detail'),
    path('osoba/', views.CreateOsobaView.as_view(), name='create-osoba'),
    path('osoba/filter/', views.FilterOsobaView.as_view(), name='filter-osoba'),
    path('stanowisko', views.stanowisko_list, name='stanowisko-list'),
    path('stanowisko/<int:pk>/', views.RetrieveStanowiskoView.as_view(), name='retrieve-stanowisko'),
    path('stanowisko', views.CreateStanowiskoView.as_view(), name='create-stanowisko'),
    path('stanowisko/<int:pk>/delete/', views.DestroyStanowiskoView.as_view(), name='destroy-stanowisko'),
    path('stanowisko/<int:pk>/', views.stanowisko_detail, name='stanowisko-detail'),
    path('stanowisko/create/', views.stanowisko_create, name='stanowisko-create'),
    path('stanowisko/<int:pk>/delete/', views.stanowisko_delete, name='stanowisko-delete'),
    path('stanowisko/', views.stanowisko_list, name='stanowisko-list'),
]