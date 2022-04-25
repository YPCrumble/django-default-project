from celery import Celery

app = Celery("django_default_project")
app.config_from_object("django_default_project.celeryconfig")
app.autodiscover_tasks()
