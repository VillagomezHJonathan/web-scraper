<a name="readme-top"></a>

[LinkedIn](https://www.linkedin.com/in/jonathanvillagomezhernandez/) |
[Website](https://www.jonweb.dev/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h1 align="center">Web Scraper</h3>

  <p align="center">
    A web scraping tool that can return data based on a specified structure!
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Web scraper built with Python using the Selenium and BeautifulSoup libraries. Its main function is to return an array of dictionaries structured in a specified way.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* Selenium
* BeautifulSoup

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

```python
from web_scraper import WebScraper

# instantiate class and pass in desired website
scrape = WebScraper('https://www.jonweb.dev/')

# desired structure with css selector where we can find that specified key
project_structure = {
  'title': '.title',
  'technologies': '.techs p',
  'description': '.desc',
}

# specify nearmost parent containg all of the above selectors and pass in structure dictionary
results = scrape.get_table('.ProjectCard', project_structure)

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>
