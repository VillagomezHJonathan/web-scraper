from web_scraper.scraper import WebScraper

scraper = WebScraper('https://www.google.com')
print(scraper.get_by_class('a', 'gb1', True))
