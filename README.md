# 🐉 Draco - HTTP Stress Testing Tool

![Python](https://img.shields.io/badge/Python-3.7+-yellow?logo=python)
![License](https://img.shields.io/badge/License-MIT-red)

**Draco** is a multi-threaded HTTP flood script designed for **Pydroid 3** on Android (also works on PC). It auto-installs its own dependencies, rotates randomized User-Agents, and launches massive concurrent GET requests to stress-test unprotected servers.

> ⚠️ **Effective against sites without DDoS protection** (Cloudflare, DDoS-Guard, etc.). For educational use and authorized testing only.

---

## 🔥 Features

- 📱 **Pydroid 3 Ready** – Runs natively on Android.
- ⚡ **Auto-Dependency Installer** – Automatically detects and installs `requests`, `fake_useragent`, and `pyfiglet` on first run. No manual setup.
- 🎯 **Unprotected Site Crusher** – Overwhelms older shared hosting, personal blogs, and homelab servers with raw thread power.
- 🎭 **Randomized User-Agents** – Rotates browser fingerprints to bypass basic bot filters.
- ⚡ **Massive Multi-Threading** – Fully configurable thread count.
- 🎨 **Clean CLI** – Colored output with ASCII banner.

---

## 📦 Installation & Auto-Setup

### On Android (Pydroid 3)
1. Install **Pydroid 3** from the Google Play Store.
2. Create a new file named `Draco.py`.
3. Copy and paste the entire script into the file.
4. Press **Run**.
   - The script will auto-detect missing libraries and install them via `pip`.
   - No manual dependency installation required.

### On PC (Windows/Linux)
```bash
git clone https://github.com/yourusername/draco-ddos-tool.git
cd draco-ddos-tool
python Draco.py
