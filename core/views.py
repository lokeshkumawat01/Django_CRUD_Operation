from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# 1. READ (List View)
@login_required # Prevents access unless logged in
def task_list(request):
    # ORM Query: Get tasks ONLY for the logged-in user
    tasks = Task.objects.filter(user=request.user) 
    # Count incomplete tasks
    count = tasks.filter(completed=False).count()
    
    context = {'tasks': tasks, 'count': count}
    return render(request, 'core/task_list.html', context)

# 2. CREATE
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) # Bind data to form
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Assign the logged-in user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm() # Empty form for GET request
        
    return render(request, 'core/task_form.html', {'form': form, 'title': 'Create Task'})

# 3. UPDATE
@login_required
def task_update(request, pk):
    # get_object_or_404 is a helper that returns 404 if ID not found
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # Pre-fill form with existing data
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'core/task_form.html', {'form': form, 'title': 'Update Task'})

# 4. DELETE
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
        
    return render(request, 'core/task_confirm_delete.html', {'task': task})