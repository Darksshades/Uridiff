from django.shortcuts import render
from uridiff.data.models import Question

def dashboard(request):

    a = Question(id=1, name="myq")
    questions = [a]

    context = {
        'questions' : questions
    }

    return render(request, 'home.html', context)
