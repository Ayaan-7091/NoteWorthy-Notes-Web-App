from django.contrib import admin
from .models import Note
# Register your models here.


class noteAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Note,noteAdmin)