from django.contrib import admin

from .models import TestExample

class TestAdmin(admin.ModelAdmin):
  list_display = ("nickname", "country", "poet", "person")

# Register your models here.
admin.site.register(TestExample, TestAdmin)
