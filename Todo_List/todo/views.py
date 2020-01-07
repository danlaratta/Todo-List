from django.shortcuts import render, redirect
from .models import TodoList
from .forms import CreateForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
# view list of todos
def home_redirect(*args, **kwargs):
    return redirect('/list/')


def list_tasks(request):
    item_list = TodoList.objects.all()
    context = {
        'tasks' : item_list,
    }
    return render(request, 'list.html', context)


# creates a task once form is filled out
def create_task(request):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list/')
    context = {
        'form' : form
    }
    return render(request, 'create_item.html', context)


def delete_tasks(request, task_id):
    del_task = TodoList.objects.get(id=task_id)

    if request.method == "POST":
        del_task.delete()
        return redirect('/list/')

    context = {
        'del' : del_task
    }
    return render(request, 'delete_item.html', context)











