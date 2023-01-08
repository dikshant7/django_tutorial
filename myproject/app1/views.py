from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import feature
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse('<h1>hey welcome </h1>')
    # name='dikshant'
    # feature1=feature()
    # feature1.id=0
    # feature1.name='fast'
    # feature1.details='our service is very quick'
    # context = {
    #     'name':'dikshant',
    #     'age':14
    # }
    features=feature.objects.all()

    return render(request,'index.html',{'features':features})


def counter(request):
    text=request.POST['text'] #text is the name of textarea
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if(username==''):
            messages.info(request,'plz enter username')
            return redirect('register')
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not same')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credential invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def post(request,pk):
    return render(request,'post.html',{'pk':pk})
