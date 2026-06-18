from django.shortcuts import render

from django.http import HttpResponse

from .models import Employee


def Home(request):
    peoples=[
        {'name':'John', 'age': 30},
        {'name':'Anna', 'age': 25},
        {'name':'Kalyan', 'age': 17},
        {'name':'Peter', 'age': 35},
        {'name':'Chandu' , 'age':23},
        {'name':'Peterson', 'age': 15},
                
    ]
  
    for people in peoples:
        print(people)
        
    return render(request,"index.html" , context={'peoples':peoples})


def Accounts(request):
    return HttpResponse("This is Accounts template")


def success_page(request):
    return HttpResponse("This is Success Page....!")

def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method == "POST":
        usertype=request.POST.get('usertype')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        location=request.POST.get('location')
        mobileno=request.POST.get('mobileno')
        
        Employee.objects.create(user_type=usertype,firstname=firstname,lastname=lastname,email=email,password=password,location=location,mobileno=mobileno)

        return render(request,'signup.html')