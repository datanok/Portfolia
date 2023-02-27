from django.shortcuts import render
from django.http import HttpResponse

#homepage, Signin, Signup, Dashboard, Portfolio creation, Portfolio edit
#Portfolio display, maybe profile page

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def create_portfolio(request):
    return render(request, 'base/create.html')

def display_portfolio(request):
    return render(request, 'base/display.html')