import requests
from bs4 import BeautifulSoup

class WebScraper():
    def __init__(self, url):
        self.url = url
        res = requests.get(self.url, headers=requests.utils.default_headers())
        self.soup = BeautifulSoup(res.content, 'html.parser')

    def get_elements(self, selector):
        return self.soup.select(selector)
