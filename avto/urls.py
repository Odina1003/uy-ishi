from django.urls import path
from . import views

urlpatterns = [
    path('avtos', views.avtos, name='avtos'),
    path('avto/<str:pk>', views.avtos, name="avto"),
    path('avtodelete/<str:pk>', views.avto_delete, name='avtodelete'),
    path('avtoupdate/<str:pk>', views.avto_delete, name='avtoupdate'),
]