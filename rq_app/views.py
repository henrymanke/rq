from django.http import HttpResponse
from django.shortcuts import render
import django_rq
from rq_app import tasks

def start_task_view(request):
    queue = django_rq.get_queue('default')
    job = queue.enqueue(tasks.example_task, 10)  # Task in die Warteschlange stellen
    return HttpResponse(f"Task {job.id} gestartet.")
