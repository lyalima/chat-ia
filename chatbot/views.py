import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Chat, Conversation
from utils.ia import ChatIA


class ConversationListView(LoginRequiredMixin, View):

    def get(self, request):
        conversations = request.user.conversations.all().order_by('-created_at')

        return render(
            request, 
            'chatbot/conversations.html',
            {'conversations': conversations}
        )


class NewConversationView(LoginRequiredMixin, View):

    def post(self, request):
        conversation = Conversation.objects.create(
            user=request.user,
            title=''
        )

        return redirect('chatbot-view', conversation_id=conversation.id)


class ChatBotView(LoginRequiredMixin, View):

    def __init__(self):
        self.chat_ia = ChatIA()


    def get(self, request, conversation_id, *args, **kwargs):
        conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
        conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
        chats = conversation.chats.all()

        return render(
            request, 
            'chatbot/chatbot.html', 
            {
             'chats': chats,
             'conversation': conversation,
             'conversation_selected': conversation_id,
             'conversations': conversations
            }
        )
    

    def post(self, request, conversation_id, *args, **kwargs):
        conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
        message = request.POST.get('message')
        chats = conversation.chats.all()
        context = self.chat_ia.get_chat_history(chats=chats)
        response = self.chat_ia.ask_ai(context=context, message=message)

        chat = Chat(
            conversation=conversation,
            question=message,
            response=response,
        )
        chat.save()

        if not conversation.title:
            conversation.title = self.chat_ia.generate_conversation_title(msg=message)
            conversation.save()

        return JsonResponse({'message': message, 'response': response})
