from web_scraper.scraper import WebScraper
import requests
from bs4 import BeautifulSoup

scraper = WebScraper('www.google.com')
scraper.print_url()