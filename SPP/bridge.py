import asyncio
import serial
import websockets

COM_PORT = 'COM4'
BAUD_RATE = 9600
WS_SERVER_URI = 'ws://localhost:8765'
RECONNECT_DELAY = 3

async def forward_scans():
    ser = None

    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
        print(f"[✓] Serial port opened: {COM_PORT} @ {BAUD_RATE} baud")
    except Exception as e:
        print(f"[!] Failed to open serial port: {e}")
        return

    websocket = None

    while True:
        try:
            if websocket is None:
                websocket = await websockets.connect(WS_SERVER_URI)
                print(f"[✓] Connected to WebSocket server: {WS_SERVER_URI}")

            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(f"[→] Scanned: {line}")
                await websocket.send(line)
                print(f"[→] Sent to WebSocket: {line}")

            await asyncio.sleep(0.05)

        except websockets.exceptions.ConnectionClosedError:
            print("[!] WebSocket connection closed unexpectedly. Reconnecting...")
            websocket = None
            await asyncio.sleep(RECONNECT_DELAY)

        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            if websocket is not None:
                await websocket.close()
                websocket = None
            await asyncio.sleep(RECONNECT_DELAY)

asyncio.run(forward_scans())
