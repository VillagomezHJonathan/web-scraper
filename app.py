from web_scraper import WebScraper

scrape = WebScraper('https://www.jonweb.dev/')

structure = {
  'title': '.title',
  'technologies': '.techs p',
  'description': '.desc',
}
print(scrape.get_table('.ProjectCard', structure))
