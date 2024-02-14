from django.urls import path
from .views import CustomUserViewSet,LoginView,LogoutView,user_list

urlpatterns = [
    path('',CustomUserViewSet.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('', user_list, name='user_list')
]
