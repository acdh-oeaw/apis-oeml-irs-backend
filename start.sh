#!/bin/bash
#useradd -M celery
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
python manage.py migrate --settings=apis.settings.dev
supervisord -c celery_config/celery.conf
supervisorctl -c celery_config/celery.conf start all
gunicorn apis.wsgi