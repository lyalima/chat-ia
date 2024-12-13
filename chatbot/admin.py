from django.contrib import admin
from .models import ChatBot


class ChatBotAdmin(admin.ModelAdmin):
    model = ChatBot
    list_display = ['message', 'response', 'created_at']


admin.site.register(ChatBot)
