"""Post Views"""
from django.shortcuts import render

# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime


# Global var
posts = [
    {
        'name':'Mont Blac',
        'user': 'Daniel Buitrago',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' :'https://picsum.photos/200/200/?image=903'
    },
    {
        'name':'Mont Blac',
        'user': 'Daniel Buitrago',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' :'https://picsum.photos/200/200/?image=903'
    },
    {
        'name':'Mont Blac',
        'user': 'Daniel Buitrago',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' :'https://picsum.photos/200/200/?image=903'
    },
    {
        'name':'Mont Blac',
        'user': 'Daniel Buitrago',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' :'https://picsum.photos/200/200/?image=903'
    }
]

# Create your views here.
def list_posts(request):
    # I make a loop to populate the initial page.
    content = []
    for post in posts:
        content.append("""
        <p>{name}</p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"></figure>
        """.format(**post))
    post = [1,2,3]
    return HttpResponse('<br>'.join(content))