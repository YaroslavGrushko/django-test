from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('test/details/<int:id>', views.details, name='details'),
]