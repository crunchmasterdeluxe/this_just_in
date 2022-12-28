from django.shortcuts import render
from django.views import generic
from game.models import Category, Headline, Intro
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello world, I'm ron Burgandy")

# @method_decorator(csrf_exempt,name='dispatch')
class Headlines(generic.ListView):
    model = Headline
    template_name = "prompter.html"

    def get_context_data(self, **kwargs):
        # Queries
        context = super().get_context_data(**kwargs)
        print("Category:",self.kwargs.get('category'))
        if int(self.kwargs.get('category')) == 3:
            self.headline = Headline.objects.order_by('?').all()[0]
        else:   
            self.headline = Headline.objects.filter(category=self.kwargs.get('category')).order_by('?').all()[0]
        self.intro = Intro.objects.order_by('?').values('intro')[0]

        # Context - pass to template
        context['headline'] = self.headline
        context['intro'] = self.intro
        context['category'] = self.kwargs.get('category')

        return context

    
class Categories(generic.ListView):
    model = Category
    template_name = "categories.html"

    def get_context_data(self, **kwargs):
        # Queries
        context = super().get_context_data(**kwargs)
        self.categories = Category.objects.filter(pk=3).values('name','pk').all()
        
        # Context - pass to template
        context['categories'] = self.categories

        return context

class Rules(generic.TemplateView):
    template_name = "rules.html"