from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls added by utkarsh
    path('', include('user.urls')),
]
