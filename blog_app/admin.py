from django.contrib import admin
from . models import Article,Category,Comment,Message

admin.site.register(Article)


admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title','email')
    search_fields = ('title',)


admin.site.site_header = "مدیریت وبگاه"