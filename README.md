# Chat de IA com Python e Django
O projeto é um chat de inteligência artificial feito com python, django e bootstrap.

A IA está configurada para ser um assistente de programação em python, mas isso pode ser alterado para uso com qualquer outro assunto.  

O projeto conta com funcionalidades como: 
  - Cadastro, login e logout de usuários;
  - Uso da biblioteca LangChain e integração com API da OpenAI para criar a IA;
  - Geração automática do título da conversa baseado no assunto;
  - Separação de conversas de acordo com o usuário logado.

Lembre-se de gerar uma chave de API para o projeto no site oficial da OpenAI, e criar um arquivo ".env" para colocar a chave.

Para instalar as dependências necessárias para usar o projeto, execute: 

```bash
pip install -r./requirements.txt
```

Para executar o projeto use: 

```bash
python manage.py migrate

python manage.py runserver
```

## Uso com Docker

### Requisitos 

- Docker 
- Docker Compose

### Construir e iniciar os containers

```bash
docker-compose up --build
```

A aplicação estará disponível em http://127.0.0.1:8000/.

### Executando comandos no container

```bash
docker-compose exec chat-ia <comando>
```

### Exemplo de comando: aplicar as migrações no container

```bash
docker-compose exec chat-ia python manage.py migrate
```

### Acessar o shell do container

```bash
docker exec -it chat-ia /bin/bash
```