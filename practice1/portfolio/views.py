from django.shortcuts import render

# Create your views here.
def portfolio(requset):
    return render(requset,'portfolio.html')