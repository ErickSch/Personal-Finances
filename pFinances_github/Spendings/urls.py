from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("delete_expense/<str:expense_id>/", views.delete_expense, name="delete_expense"),
    path("registry/", views.registry, name="registry"),
    path("create_expense_type/", views.create_expense_type, name="create_expense_type"),
    path("create_expense_type/delete_expense_type/<str:id_expense_type>", views.delete_expense_type, name="delete_expense_type"),
    path("statistics/", views.statistics, name="statistics"),
    path("data/", views.data, name="data"),
    path("edit_expense/<str:expense_pk>", views.edit_expense, name="edit_expense"),
]