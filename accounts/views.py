from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def singup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #login
            return redirect('articles_home')
    else :
        form = UserCreationForm()
    return render (request,'accounts/signup.html', {'form':form})
