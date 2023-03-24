set DJANGO_SETTINGS_MODULE=trading_app.settings
celery -A celerybeat:app beat --loglevel=info
