from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

@admin.register(Post)
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','comments')
    list_filter = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish',)









