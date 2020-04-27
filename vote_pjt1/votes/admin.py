from django.contrib import admin
from .models import Vote, Comment


# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']

admin.site.register(Vote, VoteAdmin)
admin.site.register(Comment)
