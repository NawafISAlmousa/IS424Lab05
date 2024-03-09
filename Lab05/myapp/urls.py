from django.urls import path
from . import views
app_name = "myapp"
urlpatterns = [
    path("", views.default, name = "default"),
    path("add", views.add, name = "add")
    ]