from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from about_us.models import Resident, Rate


def about(request):
    context = {
        'residents': Resident.objects.all()[0:4],
        'rates': Rate.objects.all()
    }
    return render_to_response('about.html', context=context)
