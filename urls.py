from views import health_check
from django.urls import path

urlpatterns = [
    path('healthz', health_check),
]
