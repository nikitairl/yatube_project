from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

# class GroupAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     list_display = ("pk", "title", "slug")
#     search_fields = ("title", "slug")
#     list_filter = ("slug",)
#     empty_value_display = "-пусто-"
    
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'text', 'pub_date', 'author',)
    search_fields = ('text',) 
    list_filter = ('pub_date',) 

admin.site.register(Group)
admin.site.register(Post, PostAdmin)
