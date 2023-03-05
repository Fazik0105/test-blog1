from django.shortcuts import render
from .models import *
# Create your views here.

def test(request):
    return render(request, 'testapp/test.html', {'genres':Genre.objects.all()})

def get_genre(request):
    pass