from django.contrib import admin
from . models import Edition, Note

admin.site.register([Edition, Note])
