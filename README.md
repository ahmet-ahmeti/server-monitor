# Server Monitor

A lightweight Flask web app that monitors server CPU, RAM, and disk stats in real time.

## Features
- CPU usage, temperature, and core count
- RAM total, used, and percentage
- Disk total, used, and percentage
- Auto-refreshes every 2 seconds
- Responsive design

## Stack
- Python / Flask
- psutil
- HTML, CSS, JavaScript

## Setup
1. Install dependencies:
    pip install flask psutil

2. Run the app:
    python3 monitor.py

3. Open in browser:
    http://<your-server-ip>:8000
