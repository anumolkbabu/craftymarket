# from django.shortcuts import render
# import viewsets
from rest_framework import viewsets

# response and decroater
from rest_framework.response import Response
from rest_framework.decorators import api_view

# import local data
from .serializers import *
from .models import GeeksModel
# login model and serializer
from login.models import Login

# http request import for frontend api call
from django.shortcuts import render
from django.http import JsonResponse


# create a viewset

def getRoutes(request):
	all_users =  Login.objects.all()
	serialized_users = [{'id': user.id, 'name': user.name} for user in all_users]
	return JsonResponse(serialized_users, safe=False)

class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = GeeksModel.objects.all()

	# specify serializer to be used
	serializer_class = GeeksSerializer

@api_view(['GET'])
def getUser(request, pk):
	# Query all user instances
    task = Login.objects.get(id=pk)

    serializer = LoginSerializer(task, many=False)

    # Return JSON response
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
	# Query all user instances
    all_users = Login.objects.all()

    # Serialize the user instances
    serialized_users = [{'id': user.id, 'name': user.name} for user in all_users]

    # Return JSON response
    return Response(serialized_users)

@api_view(['POST'])
def addUser(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
	task = Login.objects.get(id=pk)
	serializer = LoginSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
	task = Login.objects.get(id=pk)
	print(task.name)
	task.delete()
	return Response("User "+task.name+" deleted Sucessfully !")


# @api_view(['POST'])
# def addUser(request):
# 	serializer = LoginPostSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)
