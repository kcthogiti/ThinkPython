

import sys, webbrowser, requests 

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

p = open("test.txt", "wb")

for chunk in res.iter_content(100000):
	p.write(chunk)
	print chunk

p.close()