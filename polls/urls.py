from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path('osobas/', views.OsobaList.as_view()),
    #path('osobas/<int:pk>/', views.OsobaDetail.as_view()),
    #path('', views.index, name='index'),
    path('osobas/', views.osoba_list),
    path('osobas/<int:pk>/', views.osoba_detail),
    path('osobas/update/<int:pk>/', views.osoba_update),
    path('osobas/delete/<int:pk>/', views.osoba_delete),
    #path('osobas/add/', views.osoba_add),
    #path('osobas_filtered/<slug:slug>', views.osoba_list_filtered),
    path('stanowiskos/<int:pk>/', views.stanowisko_detail),
    path('stanowiskos/', views.stanowisko_list),
    path('stanowiskos/add/', views.stanowisko_add),
    path('stanowisko/<int:pk>/members', views.StanowiskoList.as_view(), name='StanowiskoList'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)