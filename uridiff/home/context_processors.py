from django.conf import settings

def debug(request):
    return {'DEBUG': getattr(settings, 'TEMPLATE_DEBUG', False)}
