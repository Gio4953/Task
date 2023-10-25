from django import forms
from .models import Client, FilterWord, Notification, Article

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'tts_enabled']

class FilterWordForm(forms.ModelForm):
    class Meta:
        model = FilterWord
        fields = ['client', 'word', 'wordAlias', 'subwordalias', 'stopword']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['client', 'sms', 'telegram', 'whatsapp', 'email', 'comment']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['site', 'client', 'insert_date', 'article_date', 'author', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_article', 'screenshot_url', 'status', 'found_word']
