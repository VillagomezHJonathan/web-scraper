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
    
    def get_by_tag(self, tag, is_find_many = False):
        result = None
        if (is_find_many):
            result = self.content.find_all(tag)
        else:
            result = self.content.find(tag)
        return result
    
    def get_by_class(self, tag, class_name, is_find_many = False):
        result = None
        if (is_find_many):
            result = self.content.find_all(tag, class_ = class_name)
        else:
            result = self.content.find(tag, class_ = class_name)
        return result
    
    def get_by_id(self, tag, id):
        return self.content.find(tag, id = id)

