import os
from decouple import config
from markdown import markdown
from langchain_openai import ChatOpenAI


class ChatIA:

    def __init__(self):
        self.__api_key = os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
        self.__model = ChatOpenAI(
            model='gpt-4o-mini',
            temperature=0,
        )
        self.__system_message_generate_title = (
            'Você é um gerador de títulos de conversas.'
            'Para cada mensagem que você receber, gere um título baseado no conteúdo da mensagem.'
            'Gere um título simples, mas que resuma bem o conteúdo principal da mensagem.'
            'Não precisa usar aspas nem especificar que é um título antes.'
        )
        self.__system_message_ask_ai = (
            'Você é um assistente responsável por tirar dúvidas sobre programação Python.'
            'Responda em formato markdown e em português brasileiro.'
        )
    

    def get_chat_history(self, chats):
        chat_history = []
        
        for chat in chats:
            chat_history.append(
                ('human', chat.question,)
            )
            chat_history.append(
                ('ai', chat.response,)
            )
        return chat_history
    

    def generate_conversation_title(self, msg):
        messages = [
            (
                'system', self.__system_message_generate_title
            ),
        ]
        messages.append(
            (
                'human',
                msg,
            )
        )
        response = self.__model.invoke(messages)

        return response.content.title()


    def ask_ai(self, context, message):
        messages = [
            (
                'system', self.__system_message_ask_ai
            ),
        ]
        messages.extend(context)
        messages.append(
            (
                'human',
                message,
            ),
        )
        response = self.__model.invoke(messages)

        return markdown(response.content, output_format='html')
