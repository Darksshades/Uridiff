from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import redirect
from uridiff.data.models import Question, UriUser
from uridiff.data.crawler import Crawler

def update_questions(request):
    c = Crawler()
    c.update_questions()

    return redirect('compare')


def remove_questions(request):
    Question.objects.all().delete()

    return redirect('compare')


def update_user(request):
    if not request.GET.get('user'):
        return HttpResponse('Missing user parameter')

    user_id = int(request.GET.get('user'))
    c = Crawler()
    user, _ = UriUser.objects.get_or_create(id=user_id)
    c.update_user_info(user)

    return redirect('compare')


def update_user_questions(request):
    if not request.GET.get('user'):
        return HttpResponse('Missing user parameter')

    user_id = int(request.GET.get('user'))
    c = Crawler()
    c.update_user_questions(user_id)

    return redirect('compare')
