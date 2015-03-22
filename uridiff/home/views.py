from django.shortcuts import render
from uridiff.data.models import Question
from uridiff.data.models import UriUser

def dashboard(request):

    questions = Question.objects.all()
    users = UriUser.objects.all()


    user1 = None
    user2 = None
    if request.GET.get('user1'):
        try:
            user1 = UriUser.objects.get(id=request.GET['user1'])
        except:
            pass

    if request.GET.get('user2'):
        try:
            user2 = UriUser.objects.get(id=request.GET['user2'])
        except:
            pass

    context = {
        'questions' : questions,
        'user1' : user1,
        'user2' : user2,
        'users' : users,
    }

    return render(request, 'compare.html', context)

def home(request):
    return render(request, 'home.html')

