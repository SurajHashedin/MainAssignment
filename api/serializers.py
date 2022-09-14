from rest_framework import serializers
from .models import *

#serilizer for Registration class 
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects_table
        fields = '__all__'
