#!/bin/bash

if [ ! -f "venv/bin/activate" ]; then
  read -p "Virtual environment not found. Create it now? (y/n): " create_venv
  if [[ "$create_venv" =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
  else
    echo "Aborted."
    exit 1
  fi
fi

source venv/bin/activate

pip install -r requirements.txt > /dev/null

echo "[1] Starting WebSocket server..."
gnome-terminal -- bash -c "source venv/bin/activate && python3 server.py; exec bash"

sleep 2

echo "[2] Starting scanner bridge..."
gnome-terminal -- bash -c "source venv/bin/activate && python3 bridge.py; exec bash"

sleep 2

echo "[3] Starting HTTP server on port 8888..."
gnome-terminal -- bash -c "source venv/bin/activate && python3 -m http.server 8888; exec bash"

sleep 2

echo "[4] Opening browser..."
xdg-open http://localhost:8888/index.html >/dev/null 2>&1

echo "[✓] All components started."
