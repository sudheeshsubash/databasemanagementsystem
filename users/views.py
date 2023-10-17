from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views import View
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from .models import ClientUser
from icecream import ic


class Home(View):
    @method_decorator(cache_control(no_cache=False, no_store=False, must_revalidate=True))
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'home.html')
        return redirect('signin')
    
    
    def post(self, request):
        logout(request)
        return redirect('signin')
    
    

class SignIn(View):
    @method_decorator(cache_control(no_cache=True, no_store=True, must_revalidate=True))
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'login.html')
    
    
    def post(self, request):
        user = authenticate(username=request.POST.get("username"),password=request.POST.get("password"))  
        if user:
            login(request,user)
            messages.success(request,"User SignIn succeessfull")
            return redirect('home')
        messages.error(request,'User Credentials is not valid')
        return redirect('signin')



class SignUp(View):
    def get(self, request):
        return render(request,'signup.html')


    def post(self, request):
        return redirect('home')



class TableList(View):
    def get(self, request):
        pass
    
    def post(self, request, tablename=None):
        if tablename:
            pass





@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
    if request.user.is_authenticated:
        return redirect("home")
    return render(request,'login.html')


@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        place = request.POST.get('place')
        password = request.POST.get('password')
        ClientUser.objects.create(
            username = username,
            password = make_password(password),
            place = place
        )
        return redirect('signin')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'signup.html')


@cache_control(no_cache=False, no_store=False, must_revalidate=True)
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signin')
    if request.user.is_authenticated:
        return render(request,'home.html')
    return redirect('signin')





