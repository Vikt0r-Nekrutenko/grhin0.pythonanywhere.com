from django.urls import path
from core import views

urlpatterns = [
    path('', views.main_page_view, name='main_page_view')
]