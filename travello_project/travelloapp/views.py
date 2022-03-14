from django.shortcuts import render


# Create your views here.
from travelloapp.models import place, team


def index(request):
    obj=place.objects.all()
    tmse=team.objects.all()
    return render(request, 'index.html',{'result':obj,'tms':tmse})
