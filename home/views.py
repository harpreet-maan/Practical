from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
from .models import FindBusiness,Trending,UserRegister


def index(request):
    finds=FindBusiness.objects.all()
    news=Trending.objects.all()

    return render(request, 'index.html',{'finds':finds,'news':news})


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def listings(request):
    return render(request, 'listings.html')


def listingssingle(request):
    return render(request, 'listings-single.html')


def login(request):
    if request.method=="POST":
        use=request.POST['email']
        pass1=request.POST['password']
        
        user=auth.authenticate(email=use,password=pass1)
        
        if user is not None:
            auth.login(request,user)
            
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['cpassword']
        username=request.POST['username']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'*Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'*Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=username
                ) 
                user.save();
                return redirect('login')
        
        else:
            messages.info(request,'*Password not matching')
            return redirect('register')
        return redirect('login')


    else:
        return render(request, 'register.html')

def list(request):
    return render(request,'list.html')