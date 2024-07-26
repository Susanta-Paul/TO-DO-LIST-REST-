from django.urls import path
from todo import views

urlpatterns=[
  path("", views.index, name="index"),
  path("all", views.all, name="all"),
  path("all/<int:id>", views.delete, name="delete"),
]