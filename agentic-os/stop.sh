#!/usr/bin/env bash
cd "$(dirname "$0")"
if [ -f .pid ] && kill -0 "$(cat .pid)" 2>/dev/null; then kill "$(cat .pid)"; rm -f .pid; echo "Gestoppt."; else rm -f .pid; echo "Lief nicht."; fi
