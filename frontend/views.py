from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    hama = Person.objects.get(full_name="Hamdi Mohamed")
    exps = Exprience.objects.all()
    projects = Project.objects.all()
    dict = {
        'hama' : hama ,
        'exps' : exps ,
        'projects' : projects ,
    }
    return render(request, 'home.html' , dict)
