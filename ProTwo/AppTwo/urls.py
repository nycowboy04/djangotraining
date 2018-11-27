from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^help/', views.help,name = 'help'  ),
]
