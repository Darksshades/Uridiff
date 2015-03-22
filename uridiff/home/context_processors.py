from django.conf import settings

def debug(request):
    return {'DEBUG': getattr(settings, 'TEMPLATE_DEBUG', False)}

def user_cookie(request):
    user_id = None
    if request.COOKIES.has_key('user_id'):
        user_id = request.COOKIES['user_id']

    return {'user_id': user_id }
