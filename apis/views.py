# from django.shortcuts import render
# import viewsets
from rest_framework import viewsets
from rest_framework import status

# response and decroater
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
# import local data
from .serializers import *
from .models import GeeksModel

# login model and serializer
from login.models import Login,Category,Product
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
    # init pagination
    paginator = PageNumberPagination()

    # get query params
    user_role = request.query_params.get('craftmaker')



    # handle user role filtering
    if user_role is not None:
        users = Login.objects.filter(craftmaker = user_role.capitalize())
    else:
        users = Login.objects.all()

    # serialize to give back response
    serializer = LoginSerializer(users, many=True)

    # Return JSON response
    return JsonResponse({'results':serializer.data})


# @api_view(['GET'])
# def getUsers(request):
#     # init pagination
#     paginator = PageNumberPagination()

#     # get query params
#     user_role = request.query_params.get('craftmaker')
#     page_size = request.query_params.get('page_size')

#     # handle pagination sizing
#     if page_size is not None:
#         paginator.page_size = page_size 
#     else:
#         paginator.page_size = 5  # Set your desired page size here

#     # handle user role filtering
#     if user_role is not None:
#         users = Login.objects.filter(craftmaker = user_role.capitalize())
#     else:
#         users = Login.objects.all()

#     # serialize to give back response
#     result_page = paginator.paginate_queryset(users, request)
#     serializer = LoginSerializer(result_page, many=True)

#     # Return JSON response
#     return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def getEmails(request):
	# Query all user instances
    # flat provides only email in list
    task = Login.objects.order_by('email').values_list('email', flat=True).distinct()
    # Serialize the user instances
    email_list = [user['email'] for user in [{'email': user} for user in task]]

    distinct_email_list = list(email_list)
    
    return JsonResponse({'results': distinct_email_list}, status=status.HTTP_200_OK)

@api_view(['POST'])
def addUser(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            modified_data =serializer.data
            if 'password' in modified_data:
                del modified_data['password']
            data_to_send = {'message': 'User added successfully', 'data': modified_data}
            return Response(data_to_send, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
                    'craftmaker': user.craftmaker
                    # Add more fields as needed
                }
                if user and passw:
                    return Response({'message':'Login Success !','data':user_data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Login.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
            except Login.MultipleObjectsReturned:
                return Response({'message': 'Duplicate Users'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

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
    return JsonResponse({'results':serializer.data}, status=status.HTTP_200_OK)

# 2. add category

@api_view(['POST'])
def addCategorys(request):
	serializer = CategorySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
#.UPDATE CATEGORY

@api_view(['PUT'])
def updateCategory(request, pk):
	task = Category.objects.get(categoryid=pk)
	serializer = CategorySerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
#delete category
@api_view(['DELETE'])
def deleteCategory(request, pk):
	task = Category.objects.get(categoryid=pk)
	print(task.categoryname)
	task.delete()
	return Response("Category "+task.categoryname+" deleted Sucessfully !")

#________________________________________Product-----------------------------------------------
#1.get product
@api_view(['GET'])
def getProduct(request):
	# Query all user instances
    task = Product.objects.all()
    
    # Serialize the user instances
    serializer = ProductSerializer(task, many=True)

    # Return JSON response
    return Response(serializer.data, status=status.HTTP_200_OK)
#2.Add product
@api_view(['POST'])
def addProduct(request):
	serializer = ProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
#_________________________________________________________order___________________________________________________
#1.get order
@api_view(['GET'])
def getOrder(request):
	
    task = Order.objects.all()
    
   
    serializer = OrderSerializer(task, many=True)

   
    return Response(serializer.data, status=status.HTTP_200_OK)
#2.Add order
@api_view(['POST'])
def addOrder(request):
	serializer = OrderSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)