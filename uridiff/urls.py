from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'uridiff.home.views.dashboard', name='home'),
    url(r'data/', include('uridiff.data.urls')),
    url(r'accounts/', include('uridiff.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)