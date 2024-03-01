from django.shortcuts import redirect, render

from EE.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)

def delete(req,id):
    c = Course.objects.get(pk=id)
    c.delete()
    return redirect('/')