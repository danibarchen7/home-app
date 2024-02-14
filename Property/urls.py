from django.urls import path
from Property import views

urlpatterns = [
    path('property/',views.PropertiesView.as_view())
]
