"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Comments.models import Comments
from django.contrib import admin
from django.urls import path,include,re_path
from chat import consumers 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('conversations/', include('chat.urls')),
    
    path('properties/',include('Property.urls')),
    path('images/',include('Images.urls')),
    path('Cure/',include('Cure.urls')),
    path('Comments/',include('Comments.urls')),
    path('Favorites/',include('Favorites.urls')),
    path('tipe/',include('Type.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('customer/',include('Customer.urls')),
    # path('ws/chat/', consumers.ChatConsumer.as_asgi()),
    path('',include('chat.urls'))
]
