from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.save_sensor_data, name='save_sensor_data'),
]
