from web_scraper import WebScraper

scrape = WebScraper('https://www.jonweb.dev/')

structure = {
  'title': '.title',
  'techs': '.techs p',
  'desc': '.desc',
}
print(scrape.get_table('.ProjectCard', structure))
