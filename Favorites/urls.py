from django.urls import path
from .views import FavoriteView

urlpatterns = [
    path('',FavoriteView.as_view())
]