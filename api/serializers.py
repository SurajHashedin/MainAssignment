from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket_requests
        fields = '__all__'


#serilizer for Registration class 
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects_table
        fields = '__all__'

class updateProjectsSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(queryset=projects_table.objects.all())
    class Meta:
        model = projects_table
        fields = ( 'project_id', 'project_title', 'project_description', 'project_creator'  )


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class issuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = issues_table
        fields = '__all__'