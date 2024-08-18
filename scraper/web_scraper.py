from bs4 import BeautifulSoup
from selenium import webdriver

class WebScraper:
    def __init__(self, url):
        self.url = url
        
    def get_elements(self, selector):
        driver = webdriver.Chrome()
        driver.get(self.url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        elems = soup.select(selector)

        driver.close()

        return elems
    
    def get_table(self, parent_selector, structure):
        parents = self.get_elements(parent_selector)
        table_arr = []

        for p in parents:
            new_dict = {}
            
            for key, val in structure.items():
                new_item = [i.get_text() for i in p.select(val)]

                if len(new_item) == 1:
                    new_dict[key] = new_item[0]
                else:
                    new_dict[key] = new_item

            table_arr.append(new_dict)

        
        
        return table_arr