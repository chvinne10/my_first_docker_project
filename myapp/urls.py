from django.urls import path
from . import views
from . import serializers

urlpatterns = [
    path('', views.regi_view, name='regi'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    # This path connects the name 'update' to the update_view function
    path('update-record/', views.update_view, name='update'),
    path('delete-record/', views.delete_view, name='delete'),  
    #api paths 
    path('api/login',views.regi_serializer, name='login_api'),
    path('api/home', views.login_api_view, name='home_api'),
    path('api/select',views.home_api_view,name='select_api'),
    path('api/delete',views.delete_api_view,name='delete_view'),
    
]