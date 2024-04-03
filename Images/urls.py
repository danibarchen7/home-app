from django.urls import path
from .views import PredictView,ProfileImage,SingleImageProfile,SinglePropertyImg

urlpatterns = [
    path('',PredictView.as_view()),
    path('<int:pk>/',SinglePropertyImg.as_view()),
    path('profileimg/',ProfileImage.as_view()),
    path('profileimg/<int:pk>',SingleImageProfile.as_view()),
]
