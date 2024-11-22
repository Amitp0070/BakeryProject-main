from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')  # Redirect back to signup page

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('register')  # Redirect back to signup page

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('register')  # Redirect back to signup page

        # Create the new user
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'accounts/register.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed login function
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Redirect back to the login page
    return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def profile(request):
    return render(request, 'accounts/profile.html')