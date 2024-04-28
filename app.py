from web_scraper import WebScraper

scrape = WebScraper('https://www.jonweb.dev/')

structure = {
  'title': '.ProjectCard .title',
  'techs': '.ProjectCard .techs p',
  'desc': '.ProjectCard .desc'
}
print(scrape.get_data())
