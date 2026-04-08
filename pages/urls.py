from django.urls import path
from pages import views 

urlpatterns = [
    path('', views.about_me_view, name= 'mission'),
    path('experience/', views.experience_view, name= 'experience'),
    
]