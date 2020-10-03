from django.urls import path,include,re_path

from . import views
urlpatterns = [
    path('', views.display_graph, name='display_graph'),
   
    path('figure1/', views.figure1, name='figure1'),
    path('figure2/', views.figure2, name='figure2'),
    path('figure3/', views.figure3, name='figure3'),

    path('figure4/', views.figure4, name='figure4'),
    path('figure5/', views.figure5, name='figure5'),
    path('figure6/', views.figure6, name='figure6'),

]



