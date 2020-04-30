from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-due_date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'The item has been added!')
            return redirect('todoapp')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todoapp/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'The item has been removed!')
    return redirect('todoapp')


def cross_off(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.completed = True
    item.save()
    return redirect('todoapp')


def uncross(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.completed = False
    item.save()
    return redirect('todoapp')


# def edit(request, item_id):
#     if request.method == 'POST':
#         item = Todo.objects.get(id=item_id)
#
#         form = TodoForm(request.POST, instance=item)
#
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Item has been edited!')
#             return redirect('todoapp')
#
#     else:
#         item = Todo.objects.get(id=item_id)
#         return render(request, 'todoapp/index.html', {'item': item})
