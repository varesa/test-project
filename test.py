import requests
import time

response = requests.get("https://ipinfo.io")
print(response.content)

while True:
    sleep(1)  # Idle here
