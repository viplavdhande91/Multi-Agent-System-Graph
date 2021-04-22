from django.urls import path,include,re_path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
   
   
    path('student_graph/', views.student_graph, name='student_graph'),

   
]



