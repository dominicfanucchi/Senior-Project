from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def frontpage(request):
    return render(request, 'project/base.html')

def speech(request):
    return render(request, 'project/speech.html')

@csrf_exempt
def chat(request):
    return render(request, 'project/base_.html')

def nlp(request):
    # if request.method == 'POST' and 'run_script' in request.POST:
    #     # import function to run
    #     from path_to_script import function_to_run
    #     # call function
    #     function_to_run() 
    #     # return user to required page
    #     return HttpResponseRedirect(reverse(project:nlp)
    return render(request, 'project/nlp.html')