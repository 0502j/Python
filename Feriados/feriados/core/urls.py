from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.natal),
    path('tiradentes', views.tiradentes)
]