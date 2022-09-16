from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken  
from .service import TicketService
from rest_framework import status
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.

#creating object to take log on server
logger = logging.getLogger(__name__)

class Register(viewsets.ViewSet, viewsets.GenericViewSet,
                              mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin
                              ):
    '''
    class to register new users
    '''
    serializer_class = userSerializer
    queryset = user.objects.all()
    def create(self, request, *args, **kwargs):
        if request.data["user_name"] is None:
            return Response({"Message": 'username is not given', "Status_Message":"Failed", "Status": 400}) 
        try:
            if request.data["user_email"]:
                email = request.data["user_email"]
        except:
            email="NONE"
        usr=User(
                username=request.data["user_name"],
                password=request.data["user_password"],
                email=email,
            )
        logger.debug('Registration is processing')
        if usr:
            usr.set_password(request.data["user_password"])
            usr.save()
            profile=user.objects.create(
                    user_name=usr,
                    user_email=email,
                )
            return Response({"Message": "Registered successfully", "Status_Message":"Success", "Status": 200})
        else:
            return Response({"Message": "Error during Signup!!", "Status_Message":"Failed", "Status": 400})


class Login(viewsets.ViewSet, viewsets.GenericViewSet,
                              mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin
                              ):
    '''
    class to generate token for existing users
    '''
    serializer_class = userSerializer
    queryset = user.objects.all()
    def create(self, request, *args, **kwargs):
        if not request.data:
            return Response({"Message": "Please provide username/password", "Status_Message":"Failed", "Status": 400})

        username=request.data.get("user_name")
        password=request.data.get("user_password")

        if username is None or password is None:
            return Response({"Message": "Invalid Credentials", "Status_Message":"Failed", "Status": 400})
        usr = User.objects.get(username=username)
        refresh = RefreshToken.for_user(usr)

        logger.debug('Token is generated')
        return Response({"Message": str(refresh.access_token), "Status_Message":"Success", "Status": 200})

class TicketRequest(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              ): 
    '''
    It accept all request of users like create,update,delete project issue etc
    '''
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = EventsLoggingSerializer
    queryset = events_log.objects.all()
    def create(self, request, *args, **kwargs):

        request_type = request.data['request_type']
        request_json = request.data['request_json']

        logger.debug('request type %s is recieved',request_type)
        try:
            events_log.objects.update_or_create(request_type=request_type, request_json=request_json )
            ticketSer = TicketService(request_type,request_json ).dispach_to_function_call_method()

        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return ticketSer
