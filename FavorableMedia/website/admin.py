from django.contrib import admin
from website.models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_filter = ['created_by', 'id', 'created_on']
    list_display = ['id', 'title', 'active', 'image_link', 'created_on']

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Blog, BlogAdmin)
