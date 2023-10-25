from django.db import models

# Model for Clients
class Client(models.Model):
    username = models.CharField(max_length=255, unique=True)
    tts_enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    class Meta:
        app_label = 'adminpanel'
# Model for Filter Words
class FilterWord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    wordAlias = models.CharField(max_length=1022)
    subwordalias = models.CharField(max_length=255, null=True, blank=True)
    stopword = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.word

# Model for Notifications
class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sms = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Notification for {self.client}"

# Model for Sites
class Site(models.Model):
    sitename = models.CharField(max_length=128)
    internal_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.sitename

# Model for Articles
class Article(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    insert_date = models.DateTimeField()
    article_date = models.DateTimeField()
    author = models.CharField(max_length=128, default='none', null=True, blank=True)
    url = models.URLField(max_length=1022)
    article_name = models.TextField()
    article_text = models.TextField()
    visitors_count = models.PositiveIntegerField(default=0)
    is_top_article = models.BooleanField(default=False)
    screenshot_url = models.URLField(max_length=90, null=True, blank=True)
    status = models.PositiveIntegerField(default=1)
    found_word = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.article_name
