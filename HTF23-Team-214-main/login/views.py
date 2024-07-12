# myapp/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, SignupForm,CustomSignUpForm
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse('home'))  # Use 'reverse' to get the URL
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rest of your signup view logic
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required  # Use the login_required decorator to protect the view
def home_view(request):
    # Access user-related data
    user = request.user  # Get the logged-in user

    # You can add any other user-related data to the context here
    context = {
        'welcome_message': f'Welcome, {user.username}!',  # Display the username
    }
    return render(request, 'home.html', context)
