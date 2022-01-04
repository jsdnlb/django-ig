"""Django-IG Views"""

# Django
from django.http import HttpResponse
from django.http.response import JsonResponse

# Utilities
from datetime import datetime


def hello_word(request):
    # The strftime() method returns a string representing date and time using date, time or datetime object.
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello there, Current server time is {now}!'.format(now=str(now)))


def test(request):
    # The module pdb defines an interactive source code debugger for Python programs. ... It also supports post-mortem debugging and can be called under program control. The debugger is extensible – it is actually defined as the class Pdb .
    # import pdb; pdb.set_trace() 
    numbers =request.GET['numbers']
    return HttpResponse(numbers)
