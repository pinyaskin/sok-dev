from django.urls import path

from . import views
# from .views import registerPage

urlpatterns = [
    path('', views.index, name='home'),
    # path('register/', registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('new-create/', views.createNumber, name='new-create'),
    path('edit/', views.editNumber, name='edit'),
    path('edit/<int:pk>', views.NumberUpdateView.as_view(), name='editor')
]