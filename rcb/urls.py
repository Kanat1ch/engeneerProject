from django.contrib import admin
from django.urls import path, include
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('cars/', include('Cars.urls')),
    path('bicycles/', include('Bicycles.urls')),
    path('accounts/', include('accounts.urls')),
]
