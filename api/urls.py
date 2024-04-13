from django.urls import path,include
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('signup/',views.add_account),
    path('accountlist/',views.get_account_detail_list,name="account_lists"),
    path('accountlist/<int:id>/',views.get_account_detail_list_single,name="account_lists"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]