from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'data/', include('uridiff.data.urls')),
    url(r'^$', 'uridiff.home.views.dashboard', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
