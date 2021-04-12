from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:show_id>', views.detail),
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>/destroy', views.destroy),
]