from rest_framework import serializers
from .models import *


class EventsLoggingSerializer(serializers.ModelSerializer):
    """
    serializer for event log table
    """
    class Meta:
        model = events_log
        fields = '__all__'

#serilizer for Registration class 
class ProjectsSerializer(serializers.ModelSerializer):
    """
    serializer for project table
    """
    class Meta:
        model = projects_table
        fields = '__all__'

class updateProjectsSerializer(serializers.ModelSerializer):
    """
    serializer for project table
    """
    project_id = serializers.PrimaryKeyRelatedField(queryset=projects_table.objects.all())
    class Meta:
        model = projects_table
        fields = ( 'project_id', 'project_title', 'project_description', 'project_creator'  )


class userSerializer(serializers.ModelSerializer):
    """
    serializer for user table
    """
    class Meta:
        model = user
        fields = '__all__'

class registerSerializer(serializers.ModelSerializer):
    """
    serializer for user  table
    """
    class Meta:
        model = user
        fields = '__all__'

class issuesSerializer(serializers.ModelSerializer):
    """
    serializer for issue table table
    """
    class Meta:
        model = issues_table
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    """
    serializer for ticket request table
    """
    class Meta:
        model = ticket_requests
        fields = '__all__'
