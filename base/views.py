from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render_to_response

from base.models import Tour, Category, Comment
from blog.forms import CommentForm
from blog.models import Blog
from main.forms import SubmitForm
from main.models import Slider, Main, ThingsToDo
from media.models import Gallery


def down_up():
    counter = 0
    for i in Tour.objects.all():
        if counter % 2 == 0:
            i.down = True
            i.save()
        else:
            i.down = False
            i.save()
        counter += 1


def index(request):
    down_up()
    context = {
        'form': SubmitForm,
        'media': Gallery.objects.all()[0:6],
        'tours': Tour.objects.all(),
        'blogs': Blog.objects.all(),
    }
    try:
        context['first'] = Slider.objects.all().order_by('-created_at')[0]
    except:
        pass
    try:
        context['thingstodo'] = ThingsToDo.objects.all()[0:2]
    except:
        pass
    try:
        context['other'] = ThingsToDo.objects.all()[2:7]
    except:
        pass
    try:
        context['main'] = Main.objects.all().order_by('-created_at')[0]
    except:
        pass
    try:
        context['slider'] = Slider.objects.all().order_by('-created_at')[1:4]
    except:
        pass
    return render(request, 'index.html', context=context)


def things_to_do(request):
    down_up()
    context = {
        'form': SubmitForm,
        'tours': ThingsToDo.objects.all()[0:9]
    }
    return render_to_response('things_to_do.html', context=context)


def tours(request):
    down_up()
    context = {
        'categories': Category.objects.all(),
        'tours': Tour.objects.all()
    }
    return render_to_response('tours.html', context=context)


def tours_by_category(request, category_id):
    counter = 0
    for i in Tour.objects.filter(category_id=category_id):
        if counter % 2 == 0:
            i.down = True
            i.save()
        else:
            i.down = False
            i.save()
        counter += 1
    context = {
        'category': Category.objects.get(id=category_id),
        'categories': Category.objects.all().exclude(id=category_id),
        'tours': Tour.objects.filter(category_id=category_id)
    }
    return render_to_response('tours_by_category.html', context=context)


def things_one(request, things_id):
    thing = ThingsToDo.objects.get(id=things_id)
    tours = Tour.objects.filter(thingstodo=thing)
    context = {
        'thing': thing,
        'tours': tours,
    }
    return render_to_response('things_one.html', context=context)


def contacts(request):
    return render_to_response('contacts.html')


def tour(request, tour_id):
    context = {
        'tour': Tour.objects.get(id=tour_id),
        'form': CommentForm,
        'count': Comment.objects.filter(tour_id=tour_id).count(),
        'comments': Comment.objects.filter(tour_id=tour_id).order_by('-date')
    }
    return render(request, 'tour.html', context=context)


def addcomment(request, tour_id):
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            text = form.cleaned_data['text']
            faq = Comment.objects.create(text=text, tour_id=tour_id)
            faq.save()
    return redirect(u'/tour/{0:s}/'.format(tour_id))
