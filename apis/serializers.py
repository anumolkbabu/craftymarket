# import serializer from rest_framework
from rest_framework import serializers
from django.contrib.auth import authenticate

# import model from models.py
from .models import GeeksModel

# login model
from login.models import Login

# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = GeeksModel
		fields = ('title', 'description','name','email')

# login serilizer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

# not required but can be used
class LoginPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def create(self,validated_data):
        return Login.objects.create(**validated_data)