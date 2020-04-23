from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    list_display_links = ['title']
    list_filter = ['created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']
    list_display_links = ['content']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
