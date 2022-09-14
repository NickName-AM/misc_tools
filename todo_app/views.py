from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from todo_app.models import Note
# Create your views here.

def todo(request):
    notes_from_db = Note.objects.all()
    return render(request, 'todo_app/general/todo.html', {'notes': notes_from_db})

def add(request):
    if request.method == "GET":
        return render(request, 'todo_app/general/add.html')
    elif request.method == "POST":
        Note.objects.create(
            heading=request.POST['heading'],
            description=request.POST['description']
        )
        return redirect('todo')

def edit(request, n_id):
    if request.method == "GET":
        return render(request, 'todo_app/general/edit.html', {'title': Note.objects.get(id=n_id)})
    elif request.method == "POST":
        # Get the note whose value is n_id
        note = Note.objects.get(id=n_id)
        note.description=request.POST['description']
        note.save()
        return redirect('todo')

def delete(request, n_id):
    note = Note.objects.get(id=n_id)
    note.delete()
    return redirect('todo')