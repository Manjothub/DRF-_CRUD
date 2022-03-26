from django.shortcuts import render

def HOME(request):
    return render(request,'user/login.html')