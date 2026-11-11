#!/usr/bin/env bash
cd "$(dirname "$0")"
if [ -f .pid ] && kill -0 "$(cat .pid)" 2>/dev/null; then echo "Läuft schon: http://127.0.0.1:8765"; exit 0; fi
nohup python3 server.py > server.log 2>&1 &
echo $! > .pid
sleep 1
echo "Gestartet: http://127.0.0.1:8765"
