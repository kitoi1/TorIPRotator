# 🔁 Tor IP Rotator

This Python script uses the [Tor network](https://www.torproject.org/) to rotate your public IP address, helping you stay anonymous and private online.

## 🚀 Features

- Uses the Tor SOCKS5 proxy to route your traffic.
- Automatically fetches your current IP address.
- Signals Tor to change your identity (IP rotation).
- Easy to configure and run in any environment.

## 📦 Requirements

Make sure you have the following installed:

- Python 3.x
- Tor (`sudo apt install tor`)
- Python packages:
  - `stem`
  - `requests`

Install Python dependencies:

```bash
pip install stem requests
