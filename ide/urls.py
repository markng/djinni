from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns('',
    url(r'^$', ProjectView.as_view(), name="home"),
)