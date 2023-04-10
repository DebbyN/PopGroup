from django.contrib import admin
from .models import Question
from .models import Choice

# Question and voting choice displayed on the website and setup in server admin.
admin.site.register(Question)

admin.site.register(Choice)

