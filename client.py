from celery import Celery
from tasks import add

print(add.delay(2,40).get(timeout=1))
