from django.shortcuts import render
from . models import Places
from . models import Staff


# Create your views here.


def demo(request):
    obj = Places.objects.all()
    obj1 = Staff.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})

