import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())
