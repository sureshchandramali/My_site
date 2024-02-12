from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser 
from apps.store.models import Product

# Create your views here.

def login(request):
    return render(request,"login.html")

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
            return redirect('product')
            print("Authenticated",user)
        else:
            context = {"form":form}
            return render(request, 'login.html',context=context)

def signup(request):
    return render (request,'signup.html')

def signup(request):
    if request.method == 'GET':
        form=UserCreationForm()
        context={"form":form}
        return render(request,'signup.html',context=context)
    else:
        print(request.POST)
        form=UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)
        

def product(request):
    return render (request,'product.html')

def addproduct(request):
     if request.user.is_authenticated:

        user = request.user
        form = Product()
        return render(request,'addproduct.html',context={'form':form})
    # return render (request,'addproduct.html')