from django.urls import path
from rest_framework import routers

from .api_views import LemmaResearchView, ListViewset

app_name = "oebl_research_backend"

urlpatterns = [
    path(r"lemmaresearch/", LemmaResearchView.as_view()),
    path(r"lemmaresearch/<crawlerid>/", LemmaResearchView),
]

router = routers.DefaultRouter()
router.register(r"listresearch", ListViewset)

urlpatterns += router.urls
