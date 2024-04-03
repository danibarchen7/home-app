from django.urls import path
from .views import FavoriteView,SingleFavoriteView

urlpatterns = [
    path('',FavoriteView.as_view()),
    path('<int:pk>/',SingleFavoriteView.as_view()),
]