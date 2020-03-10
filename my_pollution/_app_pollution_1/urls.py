from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dummy_so2", views.dummy, name="dummy"),
    #path("<int:index1>", views.index1, name="index1"),
]
