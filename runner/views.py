from django.shortcuts import render
from .models import Runner

# Create your views here.
def index(request):
    roster = Runner.objects.all()
    return render( request, 'runner/index.html', {'roster': roster})
