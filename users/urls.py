from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.SignIn.as_view(),name='signin'),
    # path('signup/',views.register,name='signup'),
    
]
