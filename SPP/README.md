# 🔗 Barcode Scanner Web Bridge

This project allows you to scan barcodes using a Bluetooth scanner (SPP or HID via COM port) and transmit them to a web interface via WebSocket.

## 🧰 Project Structure

- `bridge.py` — reads from the COM port and sends data to WebSocket.
- `server.py` — WebSocket server (port `8765`).
- `index.html` — displays scanned codes in the browser.
- `start.bat` — script to launch all components.
- `venv/` — Python virtual environment (automatically created on startup).

---

## ⚙️ Setup

1. Install [Python 3.10+](https://www.python.org/downloads/)
2. Identify the COM port your scanner is connected to.
   - In `bridge.py`, replace:
     ```python
     COM_PORT = 'COM4'
     BAUD_RATE = 9600
     ```
3. Make sure your scanner is operating in **SPP (Serial Port Profile)** mode and appears in the system as a COM device.

---

## ▶️ Launch

### 🪟 Windows:
```bat
start.bat
