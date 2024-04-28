import requests
from bs4 import BeautifulSoup

class WebScraper():
    def __init__(self, url):
        self.url = url
        res = requests.get(self.url, headers=requests.utils.default_headers())
        self.soup = BeautifulSoup(res.content, 'html.parser')

    def get_full_html(self):
        return self.soup.prettify()
    
    def get_elements(self, selector):
        elems = self.soup.select(selector)
        return [e.get_text() for e in elems]
    
    def get_table(self, dict):
        table_arr = []
        temp_dict = {}

        for key, val in dict.items():
            elems = self.get_elements(val)
            temp_dict[key] = elems
        
        for key, val in temp_dict.items():
            for j in range(len(temp_dict[key])):
                if len(table_arr) < len(temp_dict[key]):
                    table_arr.append({key: temp_dict[key][j]})
                else:
                    table_arr[j][key] = temp_dict[key][j]
                    
        return table_arr