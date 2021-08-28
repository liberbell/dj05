from django.urls import path, include
from . import views

app_name = "diary"

urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("add/", views.add, name="add"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("detail/<int:pk>", views.detail, name="detail"),
]
