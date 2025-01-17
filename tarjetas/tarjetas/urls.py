from django.contrib import admin
from django.urls import path
from backend.views import predecir_fraude
from frontend.views import predecir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/predecir_fraude/', predecir_fraude, name='predecir_fraude'),
    path('predecir/', predecir, name='predecir'),
]
