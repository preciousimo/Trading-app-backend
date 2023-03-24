web: gunicorn trading_app.wsgi --log-file -
worker: celery -A trading_app worker -l info