from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registration(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        
        return redirect('Home')
    
    return render(request, 'signup.html')

def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['pwd']
        
        user = authenticate(username = username,password = password)
        
        if user is not None:
            login(request, user = user)
            
            return redirect('Home')
        else:
            return render(request, 'userlogin.html')
        
    return render(request, 'userlogin.html')

def logout_user(request):
    logout(request)
    
    return redirect('login')
        

