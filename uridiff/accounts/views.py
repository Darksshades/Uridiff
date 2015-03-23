from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from uridiff.data.models import UriUser
from uridiff.data.views import update_user

def save_user(request):

    response = redirect('home')

    print "Saving user..."

    if request.GET.get('user'):
        print "Cookie set: " + request.GET.get('user')
        response.set_cookie('user_id', request.GET.get('user'))

        try:
            user_id = int(request.GET.get('user'))
        except:
            return response

        update_user(request)

    if request.COOKIES.has_key('user_id'):
        print "Old cookie: " + request.COOKIES['user_id']

    return response

def remove_user(request):

    response = redirect('home')

    response.delete_cookie('user_id')

    return response