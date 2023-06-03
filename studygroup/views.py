from django.shortcuts import render, redirect
from .models import *

def Main(request):
    return render(request, "studygroup/main.html")

def Posting(request,studyName):
    return render(request, 'studygroup/posting.html')

def NewPosting(request):
    return render(request, 'studygroup/newposting.html')