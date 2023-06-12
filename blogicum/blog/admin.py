from django.contrib import admin

from .models import Category, Location, Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'is_published',
        'description',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'pub_date',
        'author',
        'category',
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
