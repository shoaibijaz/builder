from django.conf.urls import patterns, url
from web.public.views import *

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^about', AboutView.as_view(), name='about'),
                       url(r'^contact', ContactView.as_view(), name='contact'),
)