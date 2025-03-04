from django.urls import path
from .views import ConversationListView, NewConversationView, ChatBotView 


urlpatterns = [
    path('new_conversation/', NewConversationView.as_view(), name='new-conversation-view'),
    path('conversations/', ConversationListView.as_view(), name='conversations-list-view'),
    path('chat/<int:conversation_id>/', ChatBotView.as_view(), name='chatbot-view'),
]
