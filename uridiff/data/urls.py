from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^update-questions$', 'uridiff.data.views.update_questions',
        name='update_questions'),
    url(r'^remove-questions$', 'uridiff.data.views.remove_questions',
        name='remove_questions'),
)
