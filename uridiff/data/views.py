from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import redirect
from uridiff.data.models import Question, UriUser
from uridiff.data.crawler import Crawler

def update_questions(request):
    pages = 1
    if request.GET.get('pages'):
        pages = request.GET.get('pages')

    call_command('update_data', pages=pages, interactive=False, verbosity=0)

    return redirect('home')


def remove_questions(request):
    Question.objects.all().delete()

    return redirect('home')


def update_user(request):
    if not request.GET.get('user'):
        return HttpResponse('Missing user parameter')

    user_id = int(request.GET.get('user'))
    c = Crawler()
    user, _ = UriUser.objects.get_or_create(id=user_id)
    c.update_user_info(user)

    return redirect('home')
