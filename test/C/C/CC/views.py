from django.shortcuts import render

from CC.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)

def search_name(req):
    name = req.GET.get('name')
    context = {
        'search_name': Course.objects.filter(name=name)
    }
    return render(req, 'search_name.html',context)