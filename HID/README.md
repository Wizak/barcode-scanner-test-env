# 🔗 Barcode Scanner Web HID Integration

This project supports barcode scanners that operate in **HID mode** — where the scanner behaves like a keyboard and types scanned data.

## 🧰 How It Works

In HID mode, the scanner "types" the scanned barcode data as if it were keyboard input. This method does **not require any Bluetooth pairing or custom Web APIs** — it works in any browser that accepts keyboard input.

---

## 🚀 Getting Started

### Step 1: Open the Interface

1. Open `index.html` in any modern web browser (Chrome, Edge, Firefox, etc).

---

### Step 2: Scan Barcodes

You have two options for capturing scanned codes:

#### ✅ Option 1: Manual Focus (Input Field)

- Click on an input field in the web page.
- Start scanning — the scanner will "type" the barcode into the focused field.

#### 🚫 Option 2: Automatic Capture (No Focus Needed)

- If supported by the page logic, the browser will detect incoming HID keystrokes **even if no field is focused**.
- This works best when the page listens for global `keydown` or `input` events to collect barcode data.

> Make sure your scanner is configured to send a **carriage return (Enter)** after each scan — many pages rely on it to detect scan completion.

---

## ⚠️ Notes

- HID scanners do not require any drivers or pairing — just plug and scan.
- Works on all platforms (Windows, macOS, Linux, ChromeOS).
- Ensure the scanner is in **HID (Keyboard Emulation)** mode — consult your scanner’s manual.

---

## 📦 Files

- `index.html` — Web interface that listens for HID input from a scanner.

---

