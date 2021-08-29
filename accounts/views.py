from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm

# Create your views here.
def singup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #login
            return redirect('articles_home')
    else:
        form = UserCreationForm()
    return render (request,'accounts/signup.html', {'form':form})

def signin_page(request):
    return render (request, 'accounts/signin.html')
