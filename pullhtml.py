
import bs4, requests, webbrowser, sys

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

elems = soup.select('.r a')

numOpen = min(5, len(elems))

for i in range(numOpen):
	webbrowser.open('http://google.com' + elems[i].get('href'))

	
