from django.shortcuts import render, request
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class index(request):
    def index(request):
        return render(request, 'customer/index.html')