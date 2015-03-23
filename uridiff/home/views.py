from django.shortcuts import render
from uridiff.data.models import Question
from uridiff.data.models import UriUser
from uridiff.data.crawler import Crawler

def dashboard(request):

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

    questions1 = None
    questions2 = None

    if user1 and user2:
        c = Crawler()
        questions1, questions2 = c.compare_user(user1.id, user2.id)

    context = {
        'questions1' : questions1,
        'questions2' : questions2,
        'user1' : user1,
        'user2' : user2,
        'users' : users,
    }

    return render(request, 'compare.html', context)


def home(request):
    questions = []
    if request.COOKIES.has_key('user_id'):
        try:
            questions = Question.objects.filter(users__user_id=request.COOKIES['user_id'])
        except:
            questions = []

    return render(request, 'home.html', { 'questions': questions })
