from django.urls import path
from . import views

urlpatterns = [
    path("login",views.Login_View.as_view(),name="login"),
    path("register",views.Register_View.as_view(),name="register"),
    path("",views.home.as_view(),name="home"), 
    path("add_blog",views.add.as_view(),name="add_blog"),
    path("<int:pk>",views.content.as_view(),name="content"),
    path("<int:pk>/update",views.update.as_view(),name="update"),
    path("<int:pk>/delete",views.delete.as_view(),name="delete"),
    
    path("experiment",views.experiment.as_view(),name="experiment"),
    
]