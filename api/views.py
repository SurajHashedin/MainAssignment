from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

import logging
# Create your views here.

log = logging.getLogger(__name__)

#Create a Project.
class Projects(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              ): 
    # Api for Registrations
    serializer_class = ProjectsSerializer
    def create(self, request, *args, **kwargs):

        project_title = request.data['project_title']
        project_description = request.data['project_description']
        project_creator = request.data['project_creator'] 

        try:
            # creating row table with given data
            projects_table.objects.create(project_title= project_title, project_description= project_description, \
                project_creator= project_creator)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "CreatedProject", "Status_Message":"Success", "Status": 200})  

class getProjects(viewsets.GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin):

    #queryset = applications.objects.all()
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset = projects_table.objects.all()
        return queryset