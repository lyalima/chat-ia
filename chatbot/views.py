import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from langchain_groq import ChatGroq
from markdown import markdown
from .models import ChatBot


os.environ['GROQ_API_KEY'] = settings.GROQ_API_KEY

def home(request):
    return render(request, 'home.html')


def get_chat_history(chats):
    chat_history = []
    
    for chat in chats:
        chat_history.append(
            ('human', chat.message,)
        )
        chat_history.append(
            ('ai', chat.response,)
        )
    return chat_history


def generate_message_title(message):
    model = ChatGroq(model='llama-3.2-90b-vision-preview')
    messages = [
        (
            'system', 
            'Você é um gerador de títulos de conversas.'
            'Para cada mensagem que você receber, gere um título baseado no conteúdo da mensagem.',
        ),
    ]
    messages.append(
        (
            'human',
            message,
        )
    )
    response = model.invoke(messages)

    return response.content


def ask_ai(context, message):
    model = ChatGroq(model='llama-3.2-90b-vision-preview')
    messages = [
        (
            'system',
            'Você é um assistente responsável por tirar dúvidas sobre programação Python.'
            'Responda em formato markdown.',
        ),
    ]
    messages.extend(context)
    messages.append(
        (
            'human',
            message,
        ),
    )
    response = model.invoke(messages)

    return markdown(response.content, output_format='html')


@login_required
def chatbot(request):
    chats = ChatBot.objects.filter(user=request.user)

    if request.method == 'POST':
        context = get_chat_history(chats=chats)
        message = request.POST.get('message')
        message_title = generate_message_title(message=message)
        response = ask_ai(context=context, message=message)

        chat = ChatBot(
            user=request.user,
            message=message,
            message_title=message_title,
            response=response,
        )
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html', {'chats': chats})
