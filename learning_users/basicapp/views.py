"""This is the Django views file which controls what content gets displayed."""

from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm

# For logging in

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    """Display basic index page."""
    return render(request, 'basicapp/index.html')


@login_required
def user_logout(request):
    """Log out the user."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Create the registration view."""
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    """Create the user login."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active.")
        else:
            print("Someone tried to login and failed!")
            print("Username: {}, and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'basic_app/login.html', {})
