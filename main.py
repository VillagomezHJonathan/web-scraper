from web_scraper.scraper import WebScraper

scraper = WebScraper('https://www.google.com')
print(scraper.get_full_html())
