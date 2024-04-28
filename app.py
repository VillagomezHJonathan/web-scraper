from web_scraper import WebScraper

scrape = WebScraper('https://www.acefitness.org/resources/everyone/exercise-library/equipment/dumbbells/')

dict = {
  'name': '.exercise-card__title',
  'body_part': '.exercise-info__term--body-part dd'
}
print(scrape.get_table(dict))
