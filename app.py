from bs4 import BeautifulSoup

soup = BeautifulSoup('https://www.crummy.com/software/BeautifulSoup/bs4/doc/', 'html.parser')

print(soup.prettify())