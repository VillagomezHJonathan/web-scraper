from web_scraper import WebScraper

scrape = WebScraper('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all')


print(scrape.get_full_html())