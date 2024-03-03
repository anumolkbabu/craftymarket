# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from . import views

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
# router.register(r'employees', GeeksViewSet)

# specify URL Path for rest_framework
urlpatterns = [
	path('', views.getRoutes),
	path('get-user/<str:pk>/', views.getUser),
	path('get-users', views.getUsers),
    path('add/', views.addUser),
    path('update/<str:pk>/', views.updateUser),
    path('delete/<str:pk>/', views.deleteUser),
	path('api/login/', views.LoginAPIView.as_view(), name='api_login'),
	path('api-auth/', include('rest_framework.urls'))
]
