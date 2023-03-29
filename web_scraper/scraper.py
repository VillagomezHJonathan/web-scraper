import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        req = requests.get(self.url)
        self.content = BeautifulSoup(req.content, 'html.parser')

    def get_url(self):
        return self.url
    
    def get_full_html(self):
        return self.content.prettify()

