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