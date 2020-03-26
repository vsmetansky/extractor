# Scraper that extracts text and media

## About
Given scraper can extract text and media from any website,
just specify its start url as a command line argument. In addition, 
data is written into a file in XML format (path to file is specified
as a command line argument, defaults to data.xml file in current
directory). You can also provide number of pages you need to scrape
(defaults to 20).


## Requirements
* Python 3.6 or higher.


## Install
### Linux
1. git clone https://github.com/vsmetansky/extractor.git
1. cd extractor
2. pip3 install .


## Run
### Linux
1. extractor [-h] [-f FILE_NAME] [-n PAGE_NUM] url 