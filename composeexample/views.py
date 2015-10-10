# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll

def home(request):
    return render(request,"home.html",{})
        # return HttpResponseRedirect(reverse('polls:index'))
