from django.contrib import admin
from projects.models import Project, Tag, Review

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

