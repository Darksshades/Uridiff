from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse

def update_questions(request):
    pages = 1
    if request.GET.get('pages'):
        pages = request.GET.get('pages')

    call_command('update_data', pages=pages, interactive=False, verbosity=0)

    return HttpResponse('<h1>Questions updated!</h1>')


def clear_questions(request):
    Questions.objects.all().remove()

    return HttpResponse('<h1>Questions removed!</h1>')