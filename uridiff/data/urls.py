from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^update-questions$', 'uridiff.data.views.update_questions',
        name='update_questions'),
    url(r'^remove-questions$', 'uridiff.data.views.remove_questions',
        name='remove_questions'),
    url(r'^update-user$', 'uridiff.data.views.update_user',
        name='update_user'),
    url(r'^update-user-questions$', 'uridiff.data.views.update_user_questions',
        name='update_user_questions'),
)
