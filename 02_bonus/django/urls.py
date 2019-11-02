from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home_view, name=' home'),
    path('admin/', admin.site.urls),
]

