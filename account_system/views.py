from django.shortcuts import render,redirect
from django.core import serializers
from .models import*
from .form import* 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from products import views

# Create your views here.

def new_account(request):
    return render(request,'Signup.html')

def success(request):
    return render(request,'Success.html')


def Login_Page(request):
    # return render(request,'Login.html')
    return views.Login_Page(request)


def home(request):
    return views.first(request)
    # return render(request,'index.html')

def account_signup(request):
    if(request.method == "POST"):
        # account = AccountModel()
        signup = SignupForm(request.POST)
        if(signup.is_valid):
            signup.save()
            return redirect('/success')
        else:
            return redirect('/')
        
def getEmployee(request):
    if(request.method == "GET"):
        data = AccountModel.objects.get(id=1)
      #  jsonData = json.load(data)
        print(data.name)
        dict = {}
        dict['name'] = data.name
        dict['email'] =data.email
        
        # jsonData = serializers.serialize('json',[data],)
        # print(jsonData)
        #jsonActualData = json.loads(jsonData)
        return JsonResponse(dict,safe=False)
        

@csrf_exempt      
def login(request):
    if(request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        print('incoming-->',email)
        print('incoming-->',password)
        try:
            data = AccountModel.objects.filter(email='abc')
            print('test-->',AccountModel.objects)
            print('data-->',data)
            # request.session["email"] = data.email

            return JsonResponse({"status":"success"})
        except Exception as E:
            print(E)
            return JsonResponse({"status":"invalid"},safe=False)
   

        
        
       
        