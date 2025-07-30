from celery import shared_task
import time

@shared_task
def notify(vals):
    print('task started')
    return {'message': 'task started'}