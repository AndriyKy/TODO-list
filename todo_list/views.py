from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Tag, Task


def index(request):
    """View function for the home page of the site."""

    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags": tags,
    }

    return render(request, "todo_list/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")

