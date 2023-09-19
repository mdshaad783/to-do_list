from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        category = request.POST.get('category')
        start_date = request.POST.get('start_date')
        importance = request.POST.get('importance')

        Data.objects.create(task_name=task_name, task_description=task_description, category=category, start_date=start_date, importance=importance)
        # print(task_name,task_description,category,start_date,importance)

        queryset = Data.objects.all()
        return redirect('/tasklist')
    return render(request, 'addtask.html')

def tasklist(request):
    queryset = Data.objects.all()
    context = {'infos' : queryset}
    return render(request, 'tasklist.html', context)

def delete_task(request, id):
    # print(id)
    queryset = Data.objects.get(id = id)
    queryset.delete()
    # return render('data')
    return redirect('/tasklist')