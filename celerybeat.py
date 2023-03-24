from celery import Celery
from celery.schedules import crontab

app = Celery('trading_app')

app.conf.beat_schedule = {
    'fetch_data': {
        'task': 'trading_app.tasks.fetch_data',
        'schedule': crontab(minute='*/1'),  # Run every minute
    },
}

app.conf.timezone = 'UTC'
