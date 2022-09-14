from rest_framework import serializers
from .models import *

#serilizer for Registration class 
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects_table
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class issuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = issues_table
        fields = '__all__'