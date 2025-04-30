from django.contrib import admin
from . models import Edition, Note, Ink, Paper

admin.site.register([Edition, Note, Ink, Paper])
