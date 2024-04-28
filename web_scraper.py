import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebScraper:
    def __init__(self, url):
        self.url = url
        
    def get_elements(self, selector):
        driver = webdriver.Chrome()
        driver.get(self.url)

        data = driver.find_elements(By.CSS_SELECTOR, selector)
        elems = [d.text for d in data]

        driver.close()

        return elems
    
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