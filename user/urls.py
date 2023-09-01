from django.urls import path
from .views import SignUpView, LoginView, LogoutView,UserDetailsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'), # this is custom login and also fetches the access and refresh token
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-details/', UserDetailsView.as_view(), name='user-details'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # This is kind of default login to fetch the access and refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
