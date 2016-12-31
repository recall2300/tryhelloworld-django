from django.conf.urls import url, include
from . import views

# layout.html home button 'href' attribute
app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^areas/(?P<area>.+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>.+)/$', views.candidates),
]
