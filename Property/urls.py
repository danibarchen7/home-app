from django.urls import path
from Property import views

urlpatterns = [
    path('',views.PropertiesView.as_view()),
    path('<int:pk>',views.SingleProperty.as_view())
]
