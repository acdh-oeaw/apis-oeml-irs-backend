from django.urls import path, include
from .api_views import LemmaResearchView

app_name = "oebl_research_backend"

urlpatterns = [
    path(r"api/v1/", include("oebl_research_backend.api_urls_v1")),
]
