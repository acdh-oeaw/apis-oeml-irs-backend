from django.urls import path
from django.conf.urls import include, url

app_name = "oebl_irs_workflow"

urlpatterns = [
    path(r"api/v1/", include("oebl_irs_workflow.api_urls_v1")),
]