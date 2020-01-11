from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Project, Category
from .forms import AddTask, ProjectForm, UploadForm
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone



def index(request):
    latest_projects_list = Project.objects.order_by('-pub_date')
    return render(request, 'index.html', {'latest_projects_list': latest_projects_list})

def web(request):
    pw = Project.objects.filter(category_id = 1)
    return render(request, 'web.html', {'web_projects': pw})

def games(request):
    pw = Project.objects.filter(category_id = 2)
    return render(request, 'games.html', {'games_projects': pw})

def scripts(request):
    pw = Project.objects.filter(category_id = 3)
    return render(request, 'scripts.html', {'scripts_projects': pw})

def another(request):
    pw = Project.objects.filter(category_id = 4)
    return render(request, 'another.html', {'another_projects': pw})

def detail(request, pk):
    p = get_object_or_404(Project, pk=pk)
    form = UploadForm(request.POST)
    project = Project.objects.get(pk__iexact=pk)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=project)        
        if form.is_valid():
            form.save()          
    return render(request, 'detail.html', {'projects': p, 'form': form, 'project': project})

# def add_task(request, pk):
#     form_add = AddTask(request.POST)
#     pt = Project.objects.get(pk__iexact=pk)
#     if request.method == 'POST':
#         form_add = AddTask(request.POST, instance=pt)
        
#         if form_add.is_valid():
#             form_add.save() 
#         else:
#             form_add = AddTask()
#     return render(request, 'detail.html', {'form_add': form_add, 'pt': pt})

def create_new_project(request):
    form = ProjectForm(request.POST)
    project = Project()
    if request.method == 'POST':
        if form.is_valid():
            project = form.save(commit=False)
            project.pub_date = timezone.now()
            project.save()
            return redirect('tasks:detail', pk=project.pk)
        else:
            form = ProjectForm()
    return render(request, 'create.html', {'form': form})

def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        projects = Project.objects.filter(title__icontains = search_query)
    else:
        projects = Project.objects.all()
    return render(request, 'search.html', {'search_list': projects})


