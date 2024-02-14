from django.urls import path
from .views import CureView

urlpatterns = [
    path('',CureView.as_view())
]
