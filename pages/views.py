from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from pages.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from datetime import datetime





class login(View):
    def get(self,request):
        return render (request,"pages/login.html")
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user != None:
            return redirect ("home")
        else:
            return render (request,"pages/login.html",{"message":"Incorrect Password OR User does'nt exist"})

class register(View):
    def get(self,request):
        return render (request,"pages/register.html")
    def post(self,request):
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password1 != password2:
            context={'message':"Password didn't match"}
            return render (request,"pages/register.html",context)
        else:
            User.objects.create_user(username=username,password=password1)
            return redirect('login')


class content(DetailView):
    model = Blog
    


class home(ListView):
    model = Blog

class add(CreateView):
    model = Blog
    fields=['title','content']
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    success_url="/"


class delete(DeleteView):
    model = Blog
    template_name = "pages/delete.html"
    success_url="/"


class update(UpdateView):
    model = Blog
    template_name = "pages/edit.html"
    context_object_name="blog"
    fields=['content']
    success_url="/"

    


