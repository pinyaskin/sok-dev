from django.urls import path
from . import views

urlpatterns = [
    path('', views.webapi),
    path('categories/', views.web_category)
]