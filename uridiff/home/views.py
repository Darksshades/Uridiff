from django.shortcuts import render
from uridiff.data.models import Question

def dashboard(request):

    questions = Question.objects.all()

    context = {
        'questions' : questions
    }

    return render(request, 'home.html', context)
