from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import *

# Create your views here.
def frontpage(request):
    return render(request, 'project/base.html')

def speech(request):
    template = loader.get_template('project/speech.html')
    # return HttpResponse(template.render(request))
    # return HttpResponseRedirect('/speech/')
    return render(request, 'project/speech.html')

@csrf_exempt
def chat(request):
    template = loader.get_template('project/base_.html')
    if request.method == 'POST' and 'run_script' in request.POST:
        trans = request.POST.get("transcript")
        dict = {
            'trans': trans
        }
        # from project import main
        # if request.method == 'POST' and 'run_script' in request.POST:
        #     # import function to run
        #     from path_to_script import function_to_run
        #     # call function
        #     function_to_run() 
        #     # return user to required page
        return HttpResponse(template.render(dict, request))
        # return HttpResponseRedirect('/chat/')
        
        # return render(request, 'project/nlp.html', dict)
    # return render(request, 'project/base_.html')

def nlp(request):
    return render(request, 'project/nlp.html')