# Trabalho prático 4 - Redes de Computadores II - Sistemas de Informação - UFVJM
### Alunos: Ian Carlos Gonçalves da Conceição, Jhonathan Wallace Lacerda dos Santos e Pedro Henrique Barroso;

# Chat utilizando websockets com Python

Olá! Vamos criar um chat com websockets utilizando a linguagem Python. Esse projeto faz parte de uma atividade da disciplina de Redes de Computadores II do curso de Sistemas de Informação da UFVJM.

## TUTORIAL:

Começaremos com um pequeno passo a passo de como podemos criar um ambiente virtual. O foco é o desenvolvimento do chat, portanto não há necessidade de prolongar este tutorial com explicações quanto à criação do ambiente virtual, mas é importante que seja seguido cada passo para garantirmos certa consistência no ambiente de desenvolvimento:

<strong> Observação: Verifique se você possui o Python instalado em sua máquina. Caso não possua, você pode baixá-lo [aqui](https://www.python.org/downloads/).</strong>


<strong>Criação do ambiente virtual</strong>

Passo 1 - Criar um diretório:
```console
mkdir websocketschat
```

Passo 2 - Entrar no diretório:
```console
cd websocketschat
```
*Obs: Verifique se está no diretório correto usando o comando "pwd"
```console
pwd websocketschat
```

Passo 3 - Instalar o ambiente virtual:
<br>a. Instalação do pacote:
```console
sudo apt install python3.12-venv
```
*Observação: Pode ser que solicite que você execute o comando "sudo apt-get update"

b. Criação do Ambiente Virtual:
```console
python3 -m venv env
```

Passo 4 - Ativar o ambiente virtual:
```console
source env/bin/activate
```
Passo 5 - Instalação das dependências:
```console
pip3 install websockets
```
```console
pip3 install asyncio
```
Passo 6 - Listar os pacotes instalados:
```console
pip3 list
```
Passo 7 - Mostra os pacotes e a versão para inserir no arquivo requirements.txt:
```console
pip3 freeze
```
Passo 8 - Criação do arquivo requirements:
```console
pip3 freeze > requirements.txt
```
Passo 9 - Listar o arquivo requirements.txt:
```console
cat requirements.txt
```

Perfeito! Já temos nosso ambiente virtual criado. Agora, vamos desenvolver nosso chat de fato. Para isso precisamos de uma IDE. É aconselhado o uso do Pycharm ou do Visual Studio Code, pois estas IDE's possuem funcionalidades que serão utéis mais a frente neste tutorial:

1. Dentro da sua IDE, abra a pasta "websocketschat" que acabamos de criar e na raiz do projeto crie dois arquivos:
- main.py
- index.html (DICA: Se você criar um arquivo .html vazio, digite "!" + a função de autocompletar da sua IDE. Assim será criado a estrutura base de um arquivo .html)

2. Chegamos na parte do desenvolvimento, a seguir, vamos disponibilizar o código para aqueles que desejam apenas replicar este projeto de forma facilitada. <strong>No final deste passo a passo, você encontrará toda a explicação do código desenvolvido separadamente para que não haja confusão. De qualquer forma, o código também está comentado.</strong><br>

<br>a) Dentro do seu arquivo "main.py" cole o código a seguir:
```python
import asyncio
import websockets
import json

# Armazena as conexões ativas
connected_clients = set()

async def chat_handler(websocket):
    # Adiciona o cliente conectado à lista
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Decodifica a mensagem recebida
            data = json.loads(message)
            username = data.get("username")
            msg = data.get("message")

            # Cria o payload para ser enviado
            payload = json.dumps({"username": username, "message": msg})

            # Envia a mensagem para todos os clientes conectados
            await asyncio.gather(*[client.send(payload) for client in connected_clients if client != websocket])
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        # Remove o cliente da lista ao desconectar
        connected_clients.remove(websocket)

async def main():
    # Inicia o servidor WebSocket na porta 5000
    async with websockets.serve(chat_handler, "localhost", 5000):
        print("Servidor WebSocket iniciado na porta 5000")
        await asyncio.Future()  # Mantém o servidor rodando

if __name__ == "__main__":
    asyncio.run(main())
```
b) Dentro do seu arquivo "index.html" cole o código a seguir:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>WebSocket Chat</title>
    <style>
        /* CSS referente à estilização do chat */

        body {
            font-family: Arial, sans-serif;
            margin: 0px;
            background-color: #f4f4f4;
        }
        header {
            background-color: #28F1A7;
            color: #000;
            text-align: center;
            padding: 10px 0;
            margin-bottom: 20px;
            font-size: 1.5em;
            font-weight: bold;
        }
        #chat-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            border: 1px solid #000;
            padding: 20px 20px 0px 20px;
            height: calc(100vh - 110px);
        }
        #messages {
            height: calc(100% - 118px);
            overflow-y: scroll;
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
        }
        .message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #000;
            width: fit-content;
            max-width: calc(100% - 22px);
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        .sent {
          background-color: #28F1A7;
          align-self: flex-end;
          text-align: right;
          margin-left: auto;
        }
        .received {
            background-color: #D9D9D9;
            text-align: left;
        }
        #message-form {
            display: flex;
            padding: 20px 0px;
            gap: 20px;
        }
        #message-input {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #000;
            border-radius: 5px;
        }
        #send-button {
            background-color: #1EE79D;
            color: black;
            border: 1px solid #000;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        #username {
            border: 1px solid #000;
            border-radius: 5px;
            padding: 10px;
            width: 150px;
        }
    </style>
</head>
<body>
    <!-- Estrutura HTML do chat -->

    <header>WebSocket Chat</header>
    
    <div id="chat-container">
        <div id="messages"></div>
        <form id="message-form">
            <input type="text" id="username" placeholder="Seu nome" required>
            <input type="text" id="message-input" placeholder="Digite sua mensagem" required>
            <button type="submit" id="send-button">Enviar</button>
        </form>
    </div>

    <script>
        // Código Javascript necessário para o funcionamento do chat

        const messagesDiv = document.getElementById('messages');
        const messageForm = document.getElementById('message-form');
        const usernameInput = document.getElementById('username');
        const messageInput = document.getElementById('message-input');
        const socket = new WebSocket('ws://localhost:5000');

        socket.onopen = () => {
            console.log('Conexão com WebSocket estabelecida!');
        };

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'received');
            messageElement.textContent = `${data.username}: ${data.message}`;
            messagesDiv.appendChild(messageElement);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        };

        messageForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = usernameInput.value;
            const message = messageInput.value;
            
            if (message.trim()) {
                const messageData = {
                    username: username,
                    message: message
                };
                
                socket.send(JSON.stringify(messageData));
                
                const sentMessage = document.createElement('div');
                sentMessage.classList.add('message', 'sent');
                sentMessage.textContent = `${username}: ${message}`;
                messagesDiv.appendChild(sentMessage);
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
                
                messageInput.value = '';
            }
        });
    </script>
</body>
</html>
```

3. Temos o necessário no projeto para que possamos testar o nosso chat. No entanto, para que ele funcione corretamente, você deve se atentar a um ponto importante:

> <strong> ⚠️ Apenas abrir diretamente o arquivo "index.html" com seu navegador não irá fazer com que o chat funcione, pois o arquivo "index.html", precisa estar mesmo que em um servidor local para que comunique com a aplicação em python que está em outra porta do seu computador, fazendo com que o chat com websocket funcione corretamente. </strong>

  
> ### <strong> Alternativas que podem ser escolhidas para a abertura correta do arquivo "index.html": </strong>
>
> 1️⃣ - Utilize a extensão Live Server no Visual Studio Code. Basta colar este ID de extensão na aba de extensões para buscar a extensão correta e instalá-la: ```ritwickdey.LiveServer```
> ![image](https://github.com/user-attachments/assets/7e18735e-ac70-4a59-beb9-c0c19d117e11)
>
> 2️⃣ - Uma outra alternativa é usar o Pycharm e abrir o arquivo "index.html" no navegador através dele, como mostrado nas imagens abaixo:
> ![image](https://github.com/user-attachments/assets/1a1f113c-e902-46be-a4f3-d2609ba96619)
> ![image](https://github.com/user-attachments/assets/1ccb1a04-4a8d-4cd3-b192-1ca4b615758f)

✅ Se você seguiu corretamente os passos anteriores, já pode testar o seu chat! Abra mais de uma vez o arquivo "index.html" através de um dos procedimentos acima para simular um chat com dois ou mais usuários!

<strong> E como prometido, logo abaixo está explicação dos códigos!</strong>
