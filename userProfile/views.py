from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def userProfile(request):
    user = request.user
    return render(request, 'userProfile/profile.html', {"user": user})