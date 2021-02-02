from django.contrib import admin
from .models import (
    Author,
    Editor,
    Lemma,
    Issue,
    IssueLemma,
    LemmaStatus,
    LemmaNote,
    LemmaLabel,
)

admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Lemma)
admin.site.register(Issue)
admin.site.register(IssueLemma)
admin.site.register(LemmaStatus)
admin.site.register(LemmaNote)
admin.site.register(LemmaLabel)