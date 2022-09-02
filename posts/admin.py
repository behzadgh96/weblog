from django.contrib import admin
from .models import Post,Comment



class CommentAdminInlines(admin.TabularInline):
    model = Comment
    fields = ['text',]
    extra = 0



class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','text','is_enable','published_date','created_date','updated_date']
    inlines = [CommentAdminInlines]

admin.site.register(Post,PostAdmin)


