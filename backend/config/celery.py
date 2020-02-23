from celery import Celery
from config import celeryconfig

app = Celery('tasks.tasks', backend=celeryconfig.result_backend, broker=celeryconfig.broker_url)
app.config_from_object(celeryconfig)
import tasks.tasks