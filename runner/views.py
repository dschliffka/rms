'''
from django.shortcuts import render

# Create your views here.
def index(request):
    roster = Runner.objects.all()
    return render( request, 'runner/index.html', {'roster': roster})
'''


from django.views import generic
from .models import Runner

class IndexView(generic.ListView):
    template_name = 'runner/index.html'
    context_object_name = 'roster'

    def get_queryset(self):
        return Runner.objects.all()

class DetailView(generic.DetailView):
    model = Runner
    #template_name = 'runner/detail.html'