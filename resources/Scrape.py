from flask_restful import Resource
from flask import request
import json
from web_scraper.scraper import WebScraper

class Scrape(Resource):
    def post(self):
        req = request.get_json()
        scraper = WebScraper(req['src'])
        content = scraper.get_by_tag(req['tag'])
        print(content)
        return req['tag']