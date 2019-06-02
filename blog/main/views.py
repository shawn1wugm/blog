from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')