from django.shortcuts import redirect, render
from DD.forms import EditForm
from DD.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)

def edit(req,id):
    form = EditForm()
    c = Course.objects.get(pk=id)
    if req.method == 'POST':
        form = EditForm(req.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditForm(instance=c)
    context = {
        'c':c,
        'form':form    }
    return render(req,'edit.html',context)