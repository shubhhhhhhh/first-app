from django.urls import path,include
from api import views

urlpatterns = [
    path('signup/',views.add_account),
    path('accountlist/',views.get_account_detail_list,name="account_lists"),
    path('accountlist/<int:id>/',views.get_account_detail_list_single,name="account_lists")

    
]