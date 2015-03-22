from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import redirect
from uridiff.data.models import Question

def update_questions(request):
    pages = 1
    if request.GET.get('pages'):
        pages = request.GET.get('pages')

    call_command('update_data', pages=pages, interactive=False, verbosity=0)

    return redirect('home')


def remove_questions(request):
    Question.objects.all().delete()

    return redirect('home')
