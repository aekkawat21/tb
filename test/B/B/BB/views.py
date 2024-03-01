from django.shortcuts import render

from BB.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)

def search_id(req):
    course_id = req.GET.get('course_id')
    context = {
        'search_id': Course.objects.filter(id=course_id)
    }
    return render(req, 'search_id.html', context)