from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import RequestContext
from . import Product

def search_form(request):
    '''
	Author: Meghan Debity
	Purpose: Input form for search bar feature
	'''
    return render(request, 'product/search_form.html')

def search(request):
    '''
	Author: Meghan Debity
	Purpose: View search request
	'''
    query = request.GET.get('q')
   
    # variable products is defined by products filtered through title; title_icontains makes the search insensitive to upper/lower case
    products = Product.objects.filter(title__icontains=query)
    locations = Product.objects.filter(location__icontains=query)
    return render(request, 'product/search_result.html', {"products": products, "locations": locations})