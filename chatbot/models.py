from django.contrib.auth.models import User
from django.db import models


class ChatBot(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        null=True,
        related_name='user_chat'
    )
    message = models.TextField()
    message_title = models.TextField(null=True)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.message_title}'
