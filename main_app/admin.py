from django.contrib import admin
from . models import Edition, Note, Ink

admin.site.register([Edition, Note, Ink])
