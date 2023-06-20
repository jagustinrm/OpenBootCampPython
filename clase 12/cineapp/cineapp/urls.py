from django.contrib import admin
from django.urls import path
from directores.views import lista_directores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directores/', lista_directores, name='lista_directores'),
]