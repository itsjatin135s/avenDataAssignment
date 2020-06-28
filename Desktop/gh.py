import requests
import bs4 as bs
import urllib.request

url = str(input('URL: '))

opener = urllib.request.build_opener()
opener.add_headers = [{'User-Agent' : 'Mozilla'}]
urllib.request.install_opener(opener)

raw = requests.get(url).text
soup = bs.BeautifulSoup(raw,'html.parser')

imgs = soup.find_all('img')

links = []

for img in imgs :
    link = img.get('src')
    if 'https://' not in link:
        link = url+link
    links.append(link)

#print ('img link:'+str(len(links)))
for l in enumerate(links):
    print(l)
