# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll

def home(request):
        return HttpResponseRedirect(reverse('polls:index'))
