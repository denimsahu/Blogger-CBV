from django.urls import path
from . import views

urlpatterns = [
    path("",views.home.as_view(),name="home"),
    path("login",views.login.as_view(),name="login"),
    path("<int:pk>",views.content.as_view(),name="content"),
    path("register",views.register.as_view(),name="register"),
    path("add_blog",views.add.as_view(),name="add_blog"),
    path("<int:pk>/delete",views.delete.as_view(),name="delete"),
    path("<int:pk>/update",views.update.as_view(),name="update"),
    
]