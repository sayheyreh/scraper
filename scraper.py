import requests
from bs4 import BeautifulSoup
  
URL = "https://webscraper.io/test-sites/tables"
page = requests.get(URL)
  
soup = BeautifulSoup(page.content, 'html.parser')
for p in soup.find_all('thead'):
    th = p.find_all('th')
    print('%s %s %s %s'%(th[0].text,th[1].text,th[2].text,th[3].text));
    for p in soup.find_all('tr'):
        a = p.find_all('td')
        if len(a)==0:
            pass
        else:
            print('%s %s %s %s'% (a[0].text,a[1].text,a[2].text,a[3].text))