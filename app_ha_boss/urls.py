from django.urls import path
from . import views

app_name = "app_ha_boss"

urlpatterns = [
    path("password/", views.Password_view, name="password"),
]