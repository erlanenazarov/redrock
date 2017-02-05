from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from base.models import Tour
from main.forms import TripForm
from main.models import Hotel, TripPlanner


def tripplaner(request):
    context = {
        'form': TripForm,
        'hotels': Hotel.objects.all(),
        'tours': Tour.objects.all(),
    }
    return render(request, 'tripplaner.html', context=context)


import datetime


def post_planner(request):
    if request.method == 'POST':
        form = TripForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = request.POST.get('comment', '')
            people = form.cleaned_data['people']
            if request.POST.get('no') == 'no':
                children = 0
            else:
                children = form.cleaned_data['countchildren']
            initial = form.cleaned_data['fromdate']
            final = form.cleaned_data['todate']
            country = form.cleaned_data['country']
            phone = form.cleaned_data['phone']
            final = datetime.datetime.strptime(final, '%Y/%m/%d').strftime('%Y-%m-%d')
            initial = datetime.datetime.strptime(initial, '%Y/%m/%d').strftime('%Y-%m-%d')
            trip = TripPlanner.objects.create(name=name, email=email, people=people, comment=comment,
                                              initial=initial, final=final, children=children,
                                              country=country, phone=phone)
            if 'select' != request.POST.get('category'):
                tour_id = request.POST.get('category')
                trip.tour_id = tour_id
            for i in request.POST.getlist('hotel1'):
                trip.hotel_id = i
            for i in request.POST.getlist('hotel'):
                if i != '':
                    trip.transport = i
            trip.save()
    return render_to_response('thanks.html')
