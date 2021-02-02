from django.contrib import admin

from .models import List, ListEntry, Person

admin.site.register(List)
admin.site.register(ListEntry)
admin.site.register(Person)