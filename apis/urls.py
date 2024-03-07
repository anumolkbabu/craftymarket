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
    # used for api call front end
	path('api/login/', views.LoginAPIView.as_view(), name='api_login'),
	path('api/account/register', views.addUser),
	path('api/get-users', views.getUsers),
	path('api/get-users-emails', views.getEmails),
	# testing
	path('get-user/<str:pk>/', views.getUser),
    path('update/<str:pk>/', views.updateUser),
    path('delete/<str:pk>/', views.deleteUser),
	path('api/getcategorys/', views.getCategorys,name='api_get_categorys'),
	path('addcategory/', views.addCategorys),
	path('updateCategory/<str:pk>/', views.updateCategory),
	path('deletecategory/<str:pk>/', views.deleteCategory),
	path('api-auth/', include('rest_framework.urls'))
]
