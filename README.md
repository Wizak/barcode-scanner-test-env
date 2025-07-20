# 📦 Barcode Scanner Web Project

This project allows you to scan barcodes using different communication modes and view them in a browser. It supports:

- **HID (Keyboard Emulation)**
- **BLE (Bluetooth Low Energy with Web Bluetooth API)**
- **SPP (Serial Port Profile over Bluetooth with WebSocket Bridge)**

---

## 🔀 Modes of Operation

Before using the project, make sure your **barcode scanner is configured** in the desired mode:

| Mode | Description | Requirements |
|------|-------------|--------------|
| HID | Scanner acts as a keyboard and types barcode data | Works out-of-the-box |
| BLE | Connect via Web Bluetooth and receive data from a characteristic | Requires supported browser (e.g., Chrome) |
| SPP | Connect via serial COM port and forward data to WebSocket | Requires Python + WebSocket server |

---

## 📂 Folder Structure

Each mode has its own folder with demo setup:

- `HID/` — HTML page for scanners working in HID mode.
- `BLE/` — HTML + JavaScript for connecting via Web Bluetooth.
- `SPP/` — Python + WebSocket bridge and demo web interface.

---

## 🚀 How to Use

### Step 1: Choose the Communication Mode

1. Check your scanner's settings.
2. Set it to one of the supported modes: **HID**, **BLE**, or **SPP**.

### Step 2: Use the Corresponding Demo

- Go to the appropriate folder:
  - `HID/index.html`
  - `BLE/index.html`
  - `SPP/index.html`
- Follow the README.md in that folder for mode-specific instructions.

---

## ⚠️ Notes

- Some scanners require configuration using special barcodes from the manufacturer manual.
- BLE mode requires HTTPS or localhost to work in most browsers.
- SPP mode requires installation of Python and dependencies.

---

Happy Scanning! 🎉
