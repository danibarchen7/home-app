from django.urls import path
from .views import CommentsView,PredictView,SingleComment

urlpatterns = [
    path('',CommentsView.as_view()),
    path('com/',PredictView.as_view()),
    path('com/<int:pk>',SingleComment.as_view())
]