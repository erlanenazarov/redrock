from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from media.models import Gallery


def gallery(request):
    context = {}
    medias = Gallery.objects.all()
    print medias
    try:
        context['first'] = medias[0:2]
    except:
        pass
    try:
        context['third'] = medias[2]
    except:
        pass
    try:
        context['fourth'] = medias[3]
    except:
        pass
    try:
        context['fifth'] = medias[4:]
    except:
        pass
    return render_to_response('gallery.html', context=context)
