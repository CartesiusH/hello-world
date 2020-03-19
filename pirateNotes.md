# Project Plan
## goal:
given show name, episode number and season, download episode

## steps:
1. get all episodes
    - a tags direct child of div with les-content class
    - ata-strvid attribute
    - data server attribute
    - by link text (didn't work not specific enough)
2. determine which one is the episode we want
    - sort through title attributes
3. download that epiosde 
    - using lr download thing?

# Resourcess
Selenium Docs
https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text
//*[@attribute = "attribute_value"]

Errors with Beautiful Soup That Lead Me To Selenium
https://stackoverflow.com/questions/51082130/getting-empty-src-while-scraping/51088253
https://stackoverflow.com/questions/52521456/empty-src-attribute-returned-with-selenium-on-python

RegEx Cheat Sheet
http://regexlib.com/cheatsheet.aspx


# Old Stuff
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver.get('https://ww3.fmovie.sc/free/you-season-1/watching.html/?episode=10565')
elem = driver.find_element_by_id('iframe-embed')
print(elem.get_attribute('src'))

# Ideas for the Future
- add specify episode option
- add download option
- add email/text link option

- possible virus check?
