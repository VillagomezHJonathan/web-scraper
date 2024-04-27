from web_scraper import WebScraper

scrape = WebScraper('https://www.acefitness.org/resources/everyone/exercise-library/equipment/dumbbells/')

dict = {
  'name': 'exercise-card__title',
}
print(scrape.get_by_class('.exercise-info__term--body-part dd', True))