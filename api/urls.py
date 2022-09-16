from django.urls import include, path
from rest_framework import routers
from .views import *

# Django REST Router
router = routers.DefaultRouter()

router.register(r'register', Register, basename='Register')
router.register(r'login', Login, basename='Login')
router.register(r'ticketrequest', TicketRequest, basename='TicketRequest')


# API Urls
urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))
    

]