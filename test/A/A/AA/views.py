from django.shortcuts import render
from AA.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)