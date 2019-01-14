from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
url(r'^$', views.SchoolListView.as_view(), name = 'list'),
url(r'^create/$', views.SchoolCreateView.as_view(), name = 'create'),
url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name = 'detail'),
url(r'^update/(?P<pk>[-\w]+)/$', views.SchoolUpdateView.as_view(), name = 'update'),
url(r'^delete/(?P<pk>[-\w]+)/$', views.SchoolDeleteView.as_view(), name = 'delete'),

]
