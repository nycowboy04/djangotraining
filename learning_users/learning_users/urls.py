"""learning_users URL Configuration.

Create URL patterns to redirect users around the website.
"""
from django.conf.urls import url, include
from django.contrib import admin
from basicapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^basicapp/', include('basicapp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
