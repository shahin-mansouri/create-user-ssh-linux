from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django .contrib import auth



def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user     = authenticate(username=username, password=password)
            if user is not None:
                try:
                    auth.login(request, user)
                    return redirect(request.GET.get('next'))
                except TypeError:
                    return redirect('home')
            else:
                return render(request, 'registration/login.html', {'errorMessage': 'Username or password is not current!'})
        else:
            return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

