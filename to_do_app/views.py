from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from . forms import Todoforms
from . models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name ='task_view.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.pk})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask ')






def task_view(request):
    obj1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        obj = Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,tid):
    task=Task.objects.get(id=tid)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={'tasks':task,'form':form}

    return render(request,'edit.html',context)



