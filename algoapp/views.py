from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'algoapp/index.html')

def test_d3(request):
    return render(request,'algoapp/testd3.html')