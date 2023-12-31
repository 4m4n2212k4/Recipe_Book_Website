from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact
from home.models import NewBlog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login

# Create your views here.
def index(request):
    messages.success(request, "Hii guys , welcome to the FoodieFusion!!")

    return render(request,'index.html')
def loginUser(request):
    messages.success(request, "Hii guys , welcome to the FoodieFusion!!")

    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
    return render(request,'about.html')

def blog(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dish = request.POST.get('dish')
        Ingredients = request.POST.get('Ingredients')
        Recipe = request.POST.get('Recipe')



        blog = NewBlog(name=name, email=email, phone=phone, dish=dish,Ingredients=Ingredients, Recipe=Recipe,  date=datetime.today())
        blog.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request,'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

# def logout(request):
#     return render(request,'')