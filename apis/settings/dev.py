from .base import *
import re
import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
REDMINE_ID = "14590"
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True
FEATURED_COLLECTION_NAME = "FEATURED"
MAIN_TEXT_NAME = "ÖBL Haupttext"
BIRTH_REL_NAME = "place of birth"
DEATH_REL_NAME = "place of death"
APIS_BASE_URI = "https://apis.acdh.oeaw.ac.at/"
APIS_OEBL_BIO_COLLECTION = "ÖBL Biographie"
CSRF_HEADER_NAME = "HTTP_X_CSRFTOKEN"

CORS_ALLOW_METHODS = ("GET", "OPTIONS", "PUT", "POST", "PATCH", "DELETE")


ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get(
        "GITLAB_ENVIRONMENT_URL", os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1")
    ),
).split(",")
ALLOWED_HOSTS += ["oeml-irs-backend.acdh-dev.oeaw.ac.at"]
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

INSTALLED_APPS += [
    "oebl_irs_workflow",
    "oebl_research_backend",
    "django_celery_results",
]

CELERY_RESULT_BACKEND = "django-db"

CELERY_task_routes = {
    "app.tasks.get_obv_records": {
        "queue": "limited_queue",
        "routing_key": "limit_queue.get_obv",
    }
}


SECRET_KEY = (
    "d3j@454545()(/)@zlck/6dsaf*#sdfsaf*#sadflj/6dsfk-11$)d6ixcvjsdfsdf&-u35#ayi"
)
DEBUG = True
DEV_VERSION = False

SPECTACULAR_SETTINGS["COMPONENT_SPLIT_REQUEST"] = True
SPECTACULAR_SETTINGS["COMPONENT_NO_READ_ONLY_REQUIRED"] = True

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

MAIN_TEXT_NAME = "ÖBL Haupttext"

LANGUAGE_CODE = "de"


# APIS_COMPONENTS = ['deep learning']

# APIS_BLAZEGRAPH = ('https://blazegraph.herkules.arz.oeaw.ac.at/metaphactory-play/sparql', 'metaphactory-play', 'KQCsD24treDY')


APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]


LANGUAGE_CODE = "de"

TIME_ZONE = "Europe/Vienna"
