from django.contrib import admin

# 커스터마이징
class ArticleAdmin(admin.ModelAdmin):
    # 메뉴에서 보일 attribute 설정
    list_display = ('id', 'title', 'content')


# Register your models here.
from .models import Review
admin.site.register(Review, ArticleAdmin)


admin.site.site_header = "재구몬!"
