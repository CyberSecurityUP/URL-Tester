from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:url_id>/', views.delete_url, name='delete_url'),
]
