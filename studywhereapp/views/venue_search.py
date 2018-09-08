from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import RequestContext
from . import Venue

def search_form(request):
    '''
	Author: Deanna Vickers
	Purpose: Input form for search bar feature
	'''
    return render(request, 'venue/search_form.html')

def search(request):
    '''
	Author: Deanna Vickers
	Purpose: View search request
	'''
    query = request.GET.get('q')

    # variable venues is defined by venues filtered through title; title_icontains makes the search insensitive to upper/lower case
    venues = Venue.objects.filter(name__icontains=query)
    addresses = Venue.objects.filter(address__icontains=query)
    return render(request, 'venue/search_result.html', {"venues": venues, "addresses": addresses})