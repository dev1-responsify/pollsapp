from django.contrib import admin

# Register your models here.from django.contrib import admi

#registers models Poll, and Choice in /admin/ section of the page.
from .models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)