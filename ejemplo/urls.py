from django.urls import path
from ejemplo.views import familiar

urlpatterns = [
    path('familiares', familiar),
]
