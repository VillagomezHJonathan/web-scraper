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
  git clone --recurse-submodules https://github.com/venoblin/scripts
  ```

2. **Create settings file (for [ezdownloadsorter](https://github.com/venoblin/download-file-sorter))**

  ```sh
  cd scripts
  touch settings.json
  ```

1. **Modify `settings.json`** 

  ```json
  {
    "downloads": "/path/to/Downloads",
    "destinations": {
      ".file-extension": "/path/to/destination",
      ".file-extension": "/path/to/destination",
      ".file-extension": "/path/to/destination"
    }
  }
  ```

4. **Install scripts** 
  
  ```sh
  ./install.sh
  ```

## Usage
Put usage examples here
