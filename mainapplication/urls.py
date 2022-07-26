from django.urls import path

from . import views

urlpatterns =[
    path('user/',views.UserList.as_view(),name="user"),
    path('user/<int:pk>/',views.UserDetails.as_view()),
]