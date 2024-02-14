from django.urls import path
from .views import TipeListView ,SingleTipeView

urlpatterns = [
    path('',TipeListView.as_view()),
    path('<int:pk>',SingleTipeView.as_view())
]
