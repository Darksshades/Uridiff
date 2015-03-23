from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^save-user$', 'uridiff.accounts.views.save_user',
        name='save_user'),
    url(r'^remove-user$', 'uridiff.accounts.views.remove_user',
        name='remove_user'),
)
