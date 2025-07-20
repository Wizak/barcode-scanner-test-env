# 🔗 Barcode Scanner Web Bluetooth Bridge

This project allows scanning barcodes using a Bluetooth Low Energy (BLE) barcode scanner and transmitting them to a web interface via Web Bluetooth.

## 📲 Setup Instructions

### 🔧 Step 1: Discover Your Scanner's UUIDs

1. Download the **LightBlue** app on your smartphone:
   - [iOS – App Store](https://apps.apple.com/app/lightblue/id557428110)
   - [Android – Google Play](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer)

2. Use LightBlue to connect to your barcode scanner.

3. Locate and **note down the following values**:
   - **Service UUID**
   - **Characteristic UUID**
   - **Device name** of your scanner

4. Replace the placeholder values in your code:
   ```javascript
   const SERVICE_UUID = '0000ae30-0000-1000-8000-00805f9b34fb';        // <- Replace with your service UUID
   const SERVICE_CHAR_UUID = '0000ae02-0000-1000-8000-00805f9b34fb';   // <- Replace with your characteristic UUID
   const SCANNER_NAME = 'BARCODE SCANNER';                            // <- Replace with your scanner's name
