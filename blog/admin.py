from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    raw_id_fields = ['author']
    show_facets = admin.ShowFacets.ALWAYS
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
