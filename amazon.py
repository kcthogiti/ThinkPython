
import sys, webbrowser, bs4, requests

res = requests.get("http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "+".join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

elems = soup.select(".a-link-normal.s-access-detail-page.a-text-normal")

num = min(5, len(elems))

for i in range(num):
	webbrowser.open(elems[i].get("href"))
	
	
#adding notes to test GIT