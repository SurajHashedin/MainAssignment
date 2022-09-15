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
import logging
# Create your views here.

log = logging.getLogger(__name__)


class TicketRequest(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              ): 
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectsSerializer
    queryset = ticket_requests.objects.all()
    def create(self, request, *args, **kwargs):

        request_type = request.data['request_type']
        request_json = request.data['request_json']


        try:
            ts = TicketService(request_type,request_json ).dispach_to_function_call_method()

        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return ts 
