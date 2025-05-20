import requests
import time
from stem import Signal
from stem.control import Controller

def get_current_ip():
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        return response.json()['origin']
    except Exception as e:
        return f"Error fetching IP: {e}"

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='changeme')  # Set your Tor password or use None if no password
            controller.signal(Signal.NEWNYM)
            print("[✓] IP change signal sent to Tor")
    except Exception as e:
        print(f"[!] Failed to change IP: {e}")

if __name__ == "__main__":
    print("Starting Tor IP Rotator...\n")
    for i in range(3):  # Rotate 3 times for testing
        print(f"[{i+1}] Rotating IP...")
        change_ip()
        time.sleep(5)  # Wait for new identity to take effect
        print(f"New IP: {get_current_ip()}\n")
        time.sleep(10)
