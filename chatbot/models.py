from django.contrib.auth.models import User
from django.db import models


class Conversation(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='conversations',
        verbose_name='Conversas'
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Título'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'Usuário: {self.user} | Conversa:{self.title} | Data:{self.created_at}'


class Chat(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='chats',
        verbose_name='Chats'
    )
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversa: {self.conversation.title} | Pergunta: {self.question} | Data: {self.created_at}'
