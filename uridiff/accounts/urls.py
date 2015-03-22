from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^save-user$', 'uridiff.accounts.views.save_user',
        name='save_user'),
)
