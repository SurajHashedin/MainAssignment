from django.urls import include, path
from rest_framework import routers
from .views import *

# Django REST Router
router = routers.DefaultRouter()

router.register(r'ticketrequest', TicketRequest, basename='TicketRequest')
# router.register(r'getprojects', getProjects, basename='getProjects')
# router.register(r'updateprojects', updateProjects, basename='updateProjects')
# router.register(r'users', Users, basename='Users')
# router.register(r'getusers', getUsers,basename='getUsers')
# router.register(r'registeruser', RegisterUser,basename='RegisterUser')
# API Urls
urlpatterns = [
    #path('api/registeruser/', RegisterUser.as_view(), name="RegisterUser"),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))
    

]