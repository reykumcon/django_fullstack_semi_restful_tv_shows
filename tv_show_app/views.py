from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'add_show.html')

def create(request):
    errors = Show.objects.validator(request.POST)

    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows/')

def detail(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'detail_show.html', context)

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

def update(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows/')