from django.shortcuts import render
#from . import forms
from AppTwo.forms import UserForm

def index(request):
    return render(request,'basicapp/index.html')

def users(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")
    return render(request,'apptwo/users.html', {'form':form})
