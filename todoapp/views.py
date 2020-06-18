from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def Listview(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    lists=Task.objects.all()
    form=TaskForm()
    return render(request,'todoapp/list.html',{'lists':lists,'form':form})

def updateView(request,id):
    tasks=Task.objects.get(id=id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=TaskForm(instance=tasks)
    return render(request,'todoapp/update.html',{'form':form,'tasks':tasks})

def deleteView(request,id):
    tasks=Task.objects.get(id=id)
    if request.method=='POST':
        tasks.delete()
        return redirect('/')
    form=TaskForm()
    return render(request,'todoapp/delete.html',{'form':form,'tasks':tasks})
