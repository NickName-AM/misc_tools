from django.shortcuts import redirect, render, resolve_url
from todo_app.models import Note
from math import ceil
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def todo(request):
    notes_from_db = Note.objects.filter(noteuser=request.user)
    return render(request, 'todo_app/todo.html', {'notes': notes_from_db})

@login_required
def add(request):
    if request.method == "GET":
        return render(request, 'todo_app/add.html')
    elif request.method == "POST":
        Note.objects.create(
            heading=request.POST['heading'],
            description=request.POST['description'],
            noteuser=request.user,
        )
        return redirect('todo-home')

@login_required
def edit(request, n_id):
    note = Note.objects.get(id=n_id)
    if request.user != note.noteuser:
        messages.error(request, 'Who are you?')
        return redirect('todo-home')

    if request.method == "GET":
        return render(request, 'todo_app/edit.html', {'note': note})
    elif request.method == "POST":
        # Get the note whose value is n_id
        note = Note.objects.get(id=n_id)
        note.description=request.POST['description']
        note.save()
        return redirect('todo-home')

@login_required
def delete(request, n_id):
    note = Note.objects.get(id=n_id)
    if request.user != note.noteuser:
        messages.error(request, 'Who are you?')
        return redirect('todo-home')

    note = Note.objects.get(id=n_id)
    note.delete()
    return redirect('todo-home')