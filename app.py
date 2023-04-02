from flask import Flask
from flask_restful import Api
from web_scraper.scraper import WebScraper

app = Flask(__name__)
api = Api(app)
app.run()