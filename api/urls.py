from django.urls import path
from .views import get_erosion_stats # <--- Must match views.py exactly

urlpatterns = [
    path('erosion-stats/', get_erosion_stats, name='erosion-stats'),
]