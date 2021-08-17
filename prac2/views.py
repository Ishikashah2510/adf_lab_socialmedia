from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    html_string = '''<html>
    <body>
    <center>
    <h1>18BCE081</h1>
    <h2>Practical 2</h2>
    <h3>Generating a basic homepage</h3>
    This is a basic HTML page generated using HttpResponse i.e. without using templates
    </center>
    </body>
    </html>'''

    return HttpResponse(html_string)
