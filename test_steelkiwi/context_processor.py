from django.conf import settings

def settings_processor(request):
    return  dict(settings=settings)