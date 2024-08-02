# Project Name

A comprehensive Django project utilizing Redis and RQ for background task processing.

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Running the Application](#running-the-application)
4. [Enqueuing Tasks](#enqueuing-tasks)
5. [Running the Worker](#running-the-worker)
6. [Monitoring](#monitoring)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Redis

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/henrymanke/rq.git .
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Redis:**

   Follow the [Redis installation guide](https://redis.io/download) for your operating system.

## Setup

1. **Configure Django settings:**

   Update your `settings.py` with the required configurations, including the database and Django-RQ setup.

   ```python
   INSTALLED_APPS = [
       # other apps...
       'django_rq',
       'rq_app',
   ]

   RQ_QUEUES = {
       'default': {
           'HOST': 'localhost',
           'PORT': 6379,
           'DB': 0,
           'DEFAULT_TIMEOUT': 360,
       }
   }
   ```

2. **Migrate the database:**

   ```sh
   python manage.py migrate
   ```

3. **Create a superuser (optional):**

   ```sh
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the Django development server:**

   ```sh
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000`.

## Enqueuing Tasks

To enqueue a task, you can use Django-RQ's enqueue function. The `rq_app/urls.py` provides a test URL for enqueuing a sample task:
`http://localhost:8000/rq/test/`

### URL Configuration

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls')),
    path('rq/', include('rq_app.urls')),
]
```

```python
# rq_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.start_task_view, name="rq-test"),
]
```

### View to Enqueue Task

```python
# rq_app/views.py
import django_rq
from django.http import HttpResponse

def start_task_view(request):
    queue = django_rq.get_queue('default')
    job = queue.enqueue('rq_app.tasks.example_task', 10)
    return HttpResponse(f"Task {job.id} started.")
```

This setup enqueues the `example_task` defined in `rq_app/tasks.py` with an argument of `10`.

## Running the Worker

To process tasks in the queue, an RQ worker must be running. The worker polls the Redis queue for jobs and executes them. Start the worker with:

```sh
python manage.py rqworker default
```

### Understanding the Dependencies

- **Django:** Acts as the web framework providing the structure for the project, handling routing, database management, and more.
- **Redis:** A key-value store used as the broker to manage the task queue. It stores the queued tasks and their statuses.
- **RQ (Redis Queue):** A simple Python library for queueing jobs and processing them in the background with workers. It leverages Redis as the message broker and supports scheduling, job retry, and result storage.

## Monitoring

Django-RQ includes a built-in dashboard for monitoring queues, workers, and tasks. This can be accessed at `http://localhost:8000/django-rq/`. This dashboard provides insights into:

- Active workers
- Queued, started, and failed jobs
- Job details and logs

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*This README is designed to assist in the setup and use of a Django application integrated with Redis and RQ for task queue management.*
