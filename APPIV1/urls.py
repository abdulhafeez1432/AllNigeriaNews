from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/<str:category>', Category, name='view_category'),
    path('allcategory/', AllCategory, name='all_category'),


    
    
    
]
