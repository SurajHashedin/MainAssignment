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
            projects_table.objects.update_or_create(project_title= project_title, project_description= project_description, \
                project_creator= project_creator)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Project is created", "Status_Message":"Success", "Status": 200})  

class getProjects(viewsets.GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin):

    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset = projects_table.objects.all()
        return queryset

class Users(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              ): 
    # Api for Registrations
    serializer_class = userSerializer
    def create(self, request, *args, **kwargs):

        user_name = request.data['user_name']
        user_email = request.data['user_email']
        user_password = request.data['user_password']
        try:
            # creating row table with given data
            user.objects.update_or_create(user_name= user_name, \
                user_email= user_email, user_password=user_password )
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "User is added", "Status_Message":"Success", "Status": 200}) 

class getUsers(viewsets.GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin):

    serializer_class = userSerializer

    def get_queryset(self):
        queryset = user.objects.all()
        return queryset


########
class Issues(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              ): 
    # Api for Registrations
    serializer_class = ProjectsSerializer
    def create(self, request, *args, **kwargs):

        issue_title = request.data['issue_title']
        issue_description = request.data['issue_description']
        issue_repoter = request.data['issue_repoter'] 
        issue_type = request.data['issue_type']
        issue_assignee = request.data['issue_assignee']
        issue_status = request.data['issue_status'] 
        project_name = request.data['project_name']

        try:
            # creating row table with given data
            issues_table.objects.update_or_create(issue_title= issue_title, issue_description= issue_description, \
                issue_repoter= issue_repoter, issue_type=issue_type, issue_assignee= issue_assignee \
                issue_status=issue_status,  project_name = project_name  )
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is created", "Status_Message":"Success", "Status": 200})  

class getIssues(viewsets.GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin):

    serializer_class = issuesSerializer

    def get_queryset(self):
        queryset = issues_table.objects.all()
        return queryset