import requests
from bs4 import BeautifulSoup
r = requests.get('https://github.com')
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print('Title : '+ soup.title.string)
articles = soup.findAll('div',{'class' : 'text-right'})
print('Article : '+ articles[0].text)
