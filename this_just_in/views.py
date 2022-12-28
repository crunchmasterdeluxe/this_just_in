from django.shortcuts import render
from django.views import generic
from game.models import Category, Headline, Intro
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("""<a href="/game/categories">
<button class = "btn btn-primary">Main Menu</button>
</a>""")