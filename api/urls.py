from django.urls import path
from . import views

urlpatterns = [
    path('alltable/',views.all_table_list,name='api'),
    path('getalldata/<str:modelname>/',views.DynamicModelDataManipulationView.as_view(),name='manipulationview'),
    path('getonnedata/<str:modelname>/<int:pk>/',views.DynamicModelDataActionView.as_view(),name='actionview'),
    
]

