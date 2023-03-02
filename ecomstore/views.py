from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

def catalog(request): 
    my_context = { 'site_name': 'Modern Musician' } 
    return render(request, 'sample.html', my_context) 

def file_not_found_404(request):
    page_title = 'Page Not Found'
    return render(request, '404.html')

