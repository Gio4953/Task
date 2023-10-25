from django.contrib import admin
from .models import Client, FilterWord, Notification, Article, Site

# Admin class for Client model
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'tts_enabled')
    list_filter = ('tts_enabled',)
    search_fields = ('username',)

admin.site.register(Client, ClientAdmin)

# Admin class for FilterWord model
class FilterWordAdmin(admin.ModelAdmin):
    list_display = ('client', 'word', 'wordAlias', 'subwordalias', 'stopword')
    list_filter = ('client',)
    search_fields = ('client__username', 'word')

admin.site.register(FilterWord, FilterWordAdmin)

# Admin class for Notification model
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('client', 'sms', 'telegram', 'whatsapp', 'email', 'comment')
    list_filter = ('client',)
    search_fields = ('client__username', 'sms', 'telegram', 'whatsapp', 'email', 'comment')

admin.site.register(Notification, NotificationAdmin)

# Admin class for Article model
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('site', 'client', 'article_name', 'insert_date', 'article_date')
    list_filter = ('site', 'client', 'insert_date', 'article_date')
    search_fields = ('site__sitename', 'client__username', 'article_name', 'url')

admin.site.register(Article, ArticleAdmin)

# Admin class for Site model
class SiteAdmin(admin.ModelAdmin):
    list_display = ('sitename', 'internal_id')
    list_filter = ('internal_id',)
    search_fields = ('sitename', 'internal_id')

admin.site.register(Site, SiteAdmin)
