from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login_view),
    url(r'^success/$', views.success),
    url(r'^logout/$', views.logout),
    url(r'^home/$', views.home),
    url(r'^travel/$', views.travel),
    url(r'^travel/add/$', views.add_travel),


]
