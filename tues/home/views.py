from django.shortcuts import render

# Create your views here.
def w(request):
    return render(request,'a.html')
def q(request):
    return render(request,'b.html')