from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from blog.models import Blog, Images


def blog(request):
    context = {
        'blogs': Blog.objects.all(),
        'images': Images.objects.all()
    }
    return render_to_response('blog.html', context=context)
