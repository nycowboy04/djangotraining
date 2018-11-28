from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    myDict = {'help_text':"This is the help page."}
    return render(request,'apptwo/help.html',context=myDict)

def users(request):
    user = User.objects.order_by('last_name')
    user_dict={'user_record':user}
    return render(request,'apptwo/users.html', context=user_dict)
