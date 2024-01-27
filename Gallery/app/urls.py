from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('category/<int:cid>/', views.Category_details, name='category_detail'),
    
]