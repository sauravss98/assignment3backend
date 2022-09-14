from django.urls import path

from . import views

urlpatterns =[
    path('user/',views.UserList.as_view(),name="user"),
    path('user/create',views.CreateUser.as_view()),
    path('user/update/<int:pk>',views.UpdateUser.as_view()),
    path('user/delete/<int:pk>',views.DeleteUser.as_view()),
    # path('user/<int:pk>/',views.UserDetails.as_view()),
    path('product/',views.ProductList.as_view(),name="product"),
    path("product/<int:pk>",views.ProductDetails.as_view())
]