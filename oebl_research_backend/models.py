from django.db import models
from django.contrib.postgres.fields import ArrayField
from oebl_irs_workflow.models import Lemma as ResearchPerson, Editor


class Person(models.Model):
    irs_person = models.ForeignKey(
        ResearchPerson, on_delete=models.SET_NULL, blank=True, null=True
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    bio_note = models.TextField(blank=True, null=True)
    uris = ArrayField(models.URLField(), null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.first_name}"


class List(models.Model):
    title = models.CharField(max_length=255)
    editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} ({str(self.editor)})"


class ListEntry(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    source_id = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)
    columns_scrape = models.JSONField(null=True, blank=True)
    columns_user = models.JSONField(null=True, blank=True)
    scrape = models.JSONField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    _update_scrape_triggered = False

    def __str__(self):
        return f"{str(self.person)} - scrape {str(self.last_updated)}"

    def get_dict(self):
        res = {}
        res["name"] = getattr(self.person, "name", None)
        res["first_name"] = getattr(self.person, "first_name", None)
        res["start_date"] = getattr(self.person, "date_of_birth", None)
        res["end_date"] = getattr(self.person, "date_of_death", None)
        return res
