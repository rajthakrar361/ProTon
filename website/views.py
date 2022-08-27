
from django.shortcuts import render
import uuid
# Create your views here.
from django import views
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "website/about.html"    

class TeamView(TemplateView):
    template_name = "website/team.html"

class HomeView(TemplateView):
    template_name = "website/index2.html"    
    
    def dispatch(self, request, *args, **kwargs):
        if not request.COOKIES.get('user_uuid'):
            
            
            response = HttpResponseRedirect("/test_cookie")
            
            #return super(TemplateView, self).dispatch(request, *args, **kwargs)
            return response
        else:
            print(request.COOKIES.get('user_uuid'))
            return super(TemplateView, self).dispatch(request, *args, **kwargs)

def test_cookie(request):   
    if not request.COOKIES.get('user_uuid'):
        temp=uuid.uuid4().hex
      
        response = HttpResponseRedirect("/")
        response.set_cookie('user_uuid',temp , max_age=None)
        return response
    else:
        print(request.COOKIES.get('user_uuid'))
        return redirect('/')

        