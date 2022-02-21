import re
from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'project/base.html')

def speech(request):
    return render(request, 'project/speech.html')