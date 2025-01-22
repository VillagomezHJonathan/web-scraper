<br/>
<div align="center">
<a href="https://github.com/user/repo">
<img src=".project-images/project-logo.png" alt="Logo" height="128px">
</a>
<h3 align="center">Web Scraper</h3>
<p align="center">
A web scraping tool that can return data based on a specified structure! 
<br/>
<br/>
</p>
</div>

Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)

## About The Project
Web scraper built with Python using the Selenium and BeautifulSoup libraries. Its main function is to return an array of dictionaries structured in a specified way.

### Built With
This project was built with the following technologies:
- <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python" />

## Getting Started
### Installation
1. **Clone the repository**
  ```sh
  git clone git@github.com:venoblin/web-scraper.git
  ```

2. **Create virtual enviroment**
  ```sh
  python3 -m venv venv
  ```

3. **Activate virtual enviroment**
  ```sh
  python3 venv/bin/activate
  ```

4. **Install dependencies** 
  ```sh
  pip install -r requirements.txt
  ```

## Usage
1. **Create `scrape.py` file in the root directory of the project**
   
2. **In `scrapy.py` import `WebScraper`**
  ```py
  from web_scraper import WebScraper
  ```

3. **Instantiate class and pass in desired website**
  ```py
  scrape = WebScraper('https://www.jonweb.dev/')
  ```

4. **Define structure, the key acts as the name given to elements found with the value**
  ```py
  scrape_structure = {
    'title': '.title',
    'technologies': '.techs p',
    'description': '.desc',
  }
  ```

5. **Specify nearmost parent element containg all of the selectors in the structure and pass in structure dictionary**
  ```py
  results = scrape.get_table('.ProjectCard', project_structure)
  ```

```py
print(results)
# [
#  {
#   'title': 'Flixder', 
#   'technologies': ['React', 'SCSS', 'Node.js', 'Express', 'MongoDB'], 
#   'description': 'Dating application for movies, find new movies to watch!'
#  }, 
#  {
#   'title': 'Fit Buddy', 
#   'technologies': ['Vue', 'SCSS'], 
#   'description': 'An application used to set up your workout routine for the week!'
#  }, 
#  {
#   'title': 'Tic-Tac-Toe', 
#   'technologies': ['JavaScript', 'CSS'], 
#   'description': 'Tic-Tac-Toe game made entirely with JavaScript.'
#  }
# ]
```