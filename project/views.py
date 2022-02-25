import re
from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'project/base.html')

def speech(request):
    return render(request, 'project/speech.html')

def nlp(request):
    # if request.method == 'POST' and 'run_script' in request.POST:
    #     # import function to run
    #     from path_to_script import function_to_run
    #     # call function
    #     function_to_run() 
    #     # return user to required page
    #     return HttpResponseRedirect(reverse(project:nlp)
    return render(request, 'project/nlp.html')