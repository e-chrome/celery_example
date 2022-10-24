import time

from celery import Celery


app = Celery(backend='redis://127.0.0.1:6379/2', broker='redis://127.0.0.1:6379/1')


@app.task
def hard_function(a, b):
    print(a + b)
    time.sleep(2)
    return a + b
