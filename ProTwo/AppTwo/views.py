from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    myDict = {'help_text':"This is the help page."}
    return render(request,'apptwo/help.html',context=myDict)
