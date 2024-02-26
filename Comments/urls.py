from django.urls import path
from .views import CommentsView,PredictView

urlpatterns = [
    path('',CommentsView.as_view()),
    path('com/',PredictView.as_view())
]