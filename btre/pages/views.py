from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# import dictionary for choices
from listings.choices import price_choices, state_choices, bedroom_choices

# create a function for the index link to urls API route
from listings.models import Listing

# about page is mainly realtor=, so import realtor model
from realtors.models import Realtor

# create a function for the index link to urls API route
def index(request):
    # show 3listing only
    listings = Listing.objecs.order_by('-list_date').filter(is_published=True)[:3]
    # add choices into the object
    context = {
         #'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, "pages/index.html", context)