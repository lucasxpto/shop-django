from django.urls import path

from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('detalhes/', views.detail, name='detail'),
]