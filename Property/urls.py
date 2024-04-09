from django.urls import path
from Property import views

urlpatterns = [
    path('<int:pk>',views.PropertiesView.as_view()),
    path('singlepro/<int:pk>',views.SingleProperty.as_view()),
    path('allproperties/',views.AllProperties.as_view())
]
