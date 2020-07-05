from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate , logout 
from django.contrib import auth
# Create your views here.
def signup_user(request):
    if request.user.is_authenticated : # if user exits take to home page
        return redirect('home')
    if request.method== 'POST': #if a post method then...
        form= UserCreationForm(request.POST) #update the Post request with the detailes given...form 
        if form.is_valid: 
            form.save() # if valid save the info
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password) #authenticating a user
            return redirect('login')
        
        else:
            return render(request,'signup.html',{'form':form}) 
            
    else:
        form=UserCreationForm()
        return render (request,'signup.html',{'form':form})
    
def login_user(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None :
            login(request, user )
            return redirect('home')
        else:
            form = AuthenticationForm(request.POST)
            return render(request,'signup.html',{'form':form})
    
def logout_user(request): #never use logout as view function
    logout(request) #logout user 
    return redirect('home')



def home(request):
    
    return render (request, 'home.html')

