from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.context_processors import request

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,state_choices,bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all the realtors
    realtor = Realtor.objects.order_by('-hire_date')

    #get MVP
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtor':realtor,
        'mvp_realtor':mvp_realtor

    }

    return render(request, 'pages/about.html',context)
