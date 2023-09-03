from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm,UpdateProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from quiz.models import user_history
# Create your views here.
def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user.is_authenticated:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'signin.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    return render(request,'register.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user)
    return render(request, 'profile.html', {'profile_form': profile_form,})
