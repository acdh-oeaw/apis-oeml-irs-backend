#!/bin/bash
python manage.py migrate --settings=apis.settings.dev
supervisord -c celery_config/celery.conf
supervisorctl start all
gunicorn apis.wsgi