from django.urls import path
from . import views

urlpatterns = [
    # Clients URLs
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    # Filter Words URLs
    path('filter_words/<int:client_id>/', views.filter_word_list, name='filter_word_list'),
    path('filter_words/add/<int:client_id>/', views.add_filter_word, name='add_filter_word'),
    path('filter_words/edit/<int:filter_word_id>/', views.edit_filter_word, name='edit_filter_word'),
    path('filter_words/delete/<int:filter_word_id>/', views.delete_filter_word, name='delete_filter_word'),
    # Notifications URLs
    path('notifications/<int:client_id>/', views.notification_list, name='notification_list'),
    path('notifications/add/<int:client_id>/', views.add_notification, name='add_notification'),
    path('notifications/edit/<int:notification_id>/', views.edit_notification, name='edit_notification'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    # Articles URLs
    path('articles/<int:client_id>/', views.article_list, name='article_list'),
    path('articles/add/<int:client_id>/', views.add_article, name='add_article'),
    path('articles/edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('articles/delete/<int:article_id>/', views.delete_article, name='delete_article'),


]
