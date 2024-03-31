from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
   list_display = ['title', 'create_at', 'text']
   list_filter = ['title', 'text']
   ordering = ['title', 'create_at']
   search_fields = ['title', 'text']





