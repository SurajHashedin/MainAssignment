from django.urls import include, path
from rest_framework import routers
from .views import *

# Django REST Router
router = routers.DefaultRouter()

router.register(r'projects', Projects,basename='Projects')
router.register(r'getprojects', getProjects,basename='getProjects')
router.register(r'users', Users,basename='Users')
router.register(r'getusers', getUsers,basename='getUsers')

# API Urls
urlpatterns = [

    path('', include(router.urls)),

]