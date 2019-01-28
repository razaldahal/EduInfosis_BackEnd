from django.contrib import admin
from .models import Course,Class,Section

models = (Course,Class,Section)

admin.site.register(models)
