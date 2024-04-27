import requests
from bs4 import BeautifulSoup

class WebScraper(BeautifulSoup):
    def __init__(self, url):
        self.url = url
        res = requests.get(self.url)
        self.soup = super(res.content, 'html.parser')

    def get_url(self):
        return self.url
    
    def get_full_html(self):
        return self.soup.prettify()
    
    def get_by_tag(self, tag, is_find_many = False):
        result = None
        if (is_find_many):
            result = self.soup.find_all(tag)
        else:
            result = self.soup.find(tag).get_text()
        return result
    
    def get_by_class(self, tag, class_name, is_find_many = False):
        result = None
        if (is_find_many):
            result = self.soup.find_all(tag, class_ = class_name)
        else:
            result = self.soup.find(tag, class_ = class_name).get_text()
        return result
    
    def get_by_id(self, tag, id):
        return self.soup.find(tag, id = id).get_text()
