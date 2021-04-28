from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import os

# Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
# from django.template import RequestContext


@login_required
def index(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    # return render_to_response('home/index.html', context_instance=RequestContext(request))
    return render(request, 'home/index.html', {'username': request.user.username})

""""
class IndexList(ListView):
    template_name = 'home/index.html'
    model = User
    context_object_name = 'username'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        c = super(IndexList, self).get_context_data(**kwargs)
        # add the request to the context
        c.get( self, User.username)
        return c
"""

@login_required
def php_view(request):
    # template_name = 'home/display-php.html'
    info_php_cmd = 'php home/static/home/info.php'
    fp = os.popen(info_php_cmd)
    info_php_list = fp.readlines()
    fp.close()
    # context is a dictionary mapping template
    context = {
        'info_php_list': info_php_list,
    }
    return render(request, 'home/display-php.html', context)


def about_fts(request):
    return render(request, 'home/aboutFts.html')


def enter(request):
    return render(request, 'home/login.html')


#@login_required
#def home(request):
#    return render(request, 'home/index.html', {'username': request.user.username})


def log_out(request):
    logout(request)
    return redirect('home:enter')
