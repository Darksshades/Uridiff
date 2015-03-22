from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def save_user(request):

    response = redirect('home')

    print "Saving user..."

    if request.GET.get('user'):
        print "Cookie set"
        response.set_cookie('user_id', request.GET.get('user'))

    if request.COOKIES.has_key('user_id'):
        print request.COOKIES['user_id']

    return response