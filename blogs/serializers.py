from rest_framework import serializers
from django.contrib.auth.models import User
from blogs.models import *



class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'
  


class categorySerializers(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
       


class commentSerializers(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
        
       
