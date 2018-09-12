from django.shortcuts import render, HttpResponse
from .models import User
from django.db import connection, transaction
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    #return  HttpResponse("<h1>Shawon</h1>")
    alluser=User.objects.all()
    # lname = 'shawon'
    # sname = 'shawon10@gmail.com'
    # rawquery = "SELECT * FROM home_user WHERE name='%s' and email='%s'" % (lname, sname)
    # user = User.objects.raw(rawquery)
    return render(request,'home.html',{'user':alluser,})

def register(request):
    return render(request,'register.html')

def update(request,id):
    if (request.method=="GET"):
        print(id)
        rawquery = "SELECT * FROM home_user WHERE id='%s'" % (id)
        usr = User.objects.raw(rawquery)
        return render(request,'update.html',{'usr':usr, 'id':id})
    elif(request.method=="POST"):
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["pass"]
        alluser = User.objects.all()
        query="UPDATE home_user SET name='%s' , email='%s' , password='%s' WHERE id='%s' " %(name,email,password,id)
        usr=User.objects.raw(query)
        cursor = connection.cursor()
        cursor.execute(query)
        return render(request, 'home.html', {'user': alluser, })


def delete(request,id):
    alluser = User.objects.all()
    query = "DELETE from home_user WHERE id='%s'" %(id)
    usr = User.objects.raw(query)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'home.html', {'user': alluser, })

def submit(request):
    ls=[]
    name=request.POST["name"]
    email=request.POST["email"]
    password=request.POST["pass"]
    print(name)
    print(email)
    print(password)
    ls.append(name)
    ls.append(email)
    user=User(name=name,email=email,password=password)
    user.save()
    alluser = User.objects.all()
    return  render(request,'home.html',{'user':alluser,})