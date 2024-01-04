from django.contrib import admin
from .models import News, Category,Contact, Comment

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}

    date_hierarchy = 'publish_time'
    search_fields = ['title', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Contact)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "body", "created_time", "active"]
    list_filter = ['active', 'created_time']
    search_fields = ['user','body']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activate_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment,CommentAdmin)
