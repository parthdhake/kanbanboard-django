from .formtemplate import RegisterForm

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'userAuth/login.html')


def signup(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, 'userAuth/signup.html', context)