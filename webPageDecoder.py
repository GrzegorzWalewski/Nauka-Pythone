import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
r_html = r.text
soup = BeautifulSoup(r_html)
content_section = soup.find_all("section","content-section")
for content in content_section:
	for p in content.find_all("p"):
		if repr(p.string)!= "None":
			print(repr(p.string),"\n")