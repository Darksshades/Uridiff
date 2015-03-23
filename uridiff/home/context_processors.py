from django.conf import settings
from uridiff.data.models import UriUser

def debug(request):
    return {'DEBUG': getattr(settings, 'TEMPLATE_DEBUG', False)}

def user_cookie(request):
    user_id = None
    user = None
    if request.COOKIES.has_key('user_id'):
        user_id = request.COOKIES['user_id']

        try:
            user = UriUser.objects.get(id=user_id)
        except:
            pass

    return {'user_id': user_id, 'user': user }
