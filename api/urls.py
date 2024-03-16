from django.urls import path,include
from api import views

urlpatterns = [
    path('signup/',views.add_account)
    
]