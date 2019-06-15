from django.contrib import admin
from article.models import Article, Comment

# Register your models here.

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content','pubDateTime']
    list_filter = ['article', 'content']
    search_fields = ['content']
    '''
    list_editable = ['content']<在清單就可以更動內容
    '''
    
    class Meta:
        model = Comment

admin.site.register(Article)
admin.site.register(Comment, CommentModelAdmin)