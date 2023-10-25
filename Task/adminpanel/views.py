from django.shortcuts import render, redirect
from .models import Client, FilterWord, Notification, Article
from .forms import ClientForm, FilterWordForm, NotificationForm, ArticleForm

def admin_panel_clients(request):
    return redirect('/adminpanel/clients/')

# Views for Client
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client/add_client.html', {'form': form})

def edit_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/edit_client.html', {'form': form, 'client': client})

def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    
    return render(request, 'client/delete_client.html', {'client': client})


# Views for Filter Words
def filter_word_list(request,client_id):
    filter_words = FilterWord.objects.filter(client_id=client_id)
    return render(request, 'filter_words/filter_word_list.html', {'filter_words': filter_words, 'client_id': client_id})

def add_filter_word(request,client_id):
    if request.method == 'POST':
        form = FilterWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filter_word_list')
    else:
        form = FilterWordForm()
    return render(request, 'filter_words/add_filter_word.html', {'client_id': client_id})

def edit_filter_word(request, filter_word_id,client_id):
    filter_word = FilterWord.objects.get(id=filter_word_id)
    if request.method == 'POST':
        form = FilterWordForm(request.POST, instance=filter_word)
        if form.is_valid():
            form.save()
            return redirect('filter_word_list')
    else:
        form = FilterWordForm(instance=filter_word)
    return render(request, 'filter_words/edit_filter_word.html', {'client_id': client_id, 'filter_word': filter_word})

def delete_filter_word(request, filter_word_id,client_id):
    filter_word = FilterWord.objects.get(id=filter_word_id)
    if request.method == 'POST':
        filter_word.delete()
        return redirect('filter_word_list')

    return render(request, 'filter_words/delete_filter_word.html', {'client_id': client_id, 'filter_word': filter_word})


# Views for Notifications
def notification_list(request, client_id):
    notifications = Notification.objects.filter(client_id=client_id)
    return render(request, 'notifications/notification_list.html', {'notifications': notifications, 'client_id': client_id})

def add_notification(request,client_id):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notifications/add_notification.html', {'client_id': client_id})

def edit_notification(request, notification_id,client_id):
    notification = Notification.objects.get(id=notification_id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notifications/edit_notification.html', {'client_id': client_id, 'notification': notification})

def delete_notification(request, notification_id,client_id):
    notification = Notification.objects.get(id=notification_id)
    if request.method == 'POST':
        notification.delete()
        return redirect('notification_list')

    return render(request, 'notifications/delete_notification.html', {'client_id': client_id, 'notification': notification})

# Views for Articles
def article_list(request, client_id):
    articles = Article.objects.filter(client_id=client_id)
    return render(request, 'articles/article_list.html', {'articles': articles, 'client_id': client_id})

def add_article(request, client_id):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/add_article.html', {'client_id': client_id}, {'form': form})

def edit_article(request, article_id, client_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():  # Corrected here
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'client_id': client_id, 'article': article})


def delete_article(request, article_id, client_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')

    return render(request, 'articles/delete_article.html', {'client_id': client_id, 'article': article})
