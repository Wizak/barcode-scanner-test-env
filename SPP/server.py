import asyncio
import websockets.legacy.server

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    print("🔗 Client connected")
    try:
        async for message in websocket:
            print(f"[✓] Received: {message}")
            for c in clients:
                try:
                    await c.send(message)
                    print(f"[→] Sent to client: {message}")
                except Exception as e:
                    print(f"[!] Failed to send: {e}")
    except Exception as e:
        print(f"[!] Error in handler: {e}")
    finally:
        clients.remove(websocket)

async def main():
    print("🔌 WebSocket server running at ws://localhost:8765")
    async with websockets.legacy.server.serve(handler, 'localhost', 8765):
        await asyncio.Future()

asyncio.run(main())
