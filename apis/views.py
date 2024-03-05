# from django.shortcuts import render
# import viewsets
from rest_framework import viewsets
from rest_framework import status

# response and decroater
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# import local data
from .serializers import *
from .models import GeeksModel

# login model and serializer
from login.models import Login,Category
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

# ---------------------------------           login    -start    ----------------------------------
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
    task = Login.objects.all()
    # Serialize the user instances
    # serialized_users = [{'id': user.id, 'name': user.name} for user in all_users]

    serializer = LoginSerializer(task, many=True)

    # Return JSON response
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addUser(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

# view for signin -- check is valid emailId and password
class LoginAPIView(APIView):
    def post(self, request):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = Login.objects.get(email=email)
                passw = Login.objects.get(password=password)
                # Correct indentation for user_data
                user_data = {
                    'username': user.name,
                    'email': user.email,
					'id': user.id,
                    # Add more fields as needed
                }
                if user and passw:
                    return Response({'message':'Login Success !','data':user_data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Login.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update user details
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

# ---------------------------------           login    - end    ----------------------------------
#------------------------------------------Category-----------------------------------------------------

# 1. get categorys

@api_view(['GET'])
def getCategorys(request):
	# Query all user instances
    task = Category.objects.all()
    
    # Serialize the user instances
    serializer = CategorySerializer(task, many=True)

    # Return JSON response
    return Response(serializer.data, status=status.HTTP_200_OK)

# 2. add category

@api_view(['POST'])
def addCategorys(request):
	serializer = CategorySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#________________________________________Product-----------------------------------------------
