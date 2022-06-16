from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage,  name='login'),
    path('logout/', views.logoutUser,  name='logout'),
    path('register/', views.registerPage,  name='register'),
    
    path('', views.home, name='home'),
    
    path('room/<str:pk>/', views.room, name="room"),
    path('create_room/', views.createRoom, name="createRoom"),

    path('userProfile/<str:pk>/', views.userProfile, name="userProfile"),

    path('update_room/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path('delete_message/<str:pk>/', views.deleteMessage, name="deleteMessage"),

    path('update_user/', views.updateUser, name="updateUser"),

    path('viewTopics/', views.viewTopics, name="viewTopics"),
    path('viewActivity/', views.viewActivity, name="viewActivity"),
]