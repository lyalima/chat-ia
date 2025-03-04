from django.contrib import admin
from .models import Conversation, Chat


class ChatAdmin(admin.ModelAdmin):
    model = Chat
    list_display = ['message', 'response', 'created_at']


class ConversationAdmin(admin.ModelAdmin):
    model = Conversation
    list_display = ['user', 'title', 'created_at']


admin.site.register(Chat)
admin.site.register(Conversation)
