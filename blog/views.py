from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render_to_response

from blog.forms import CommentForm
from blog.models import Blog, Images, Comment


def blog(request):
    context = {
        'blogs': Blog.objects.all(),
        'form':CommentForm,
        'images': Images.objects.all(),
        'count': Comment.objects.all().count(),
        'comments': Comment.objects.order_by('-date')
    }
    return render(request,'blog.html', context=context)


def addcomment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            text = form.cleaned_data['text']
            faq = Comment.objects.create(text=text)
            faq.save()
    return redirect('/blog/')