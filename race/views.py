from django.shortcuts import render
from .models import Race

# Create your views here.
def index(request):
    season = Race.objects.all()
    return render( request, 'race/index.html', {'season': season})
