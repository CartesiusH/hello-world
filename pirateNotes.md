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

Using Requests Library to Download Video
https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un

Cheater way? GetFLV (or see how it works)
https://www.quora.com/Which-is-the-easiest-way-to-get-a-streaming-video-running-on-JW-player-on-the-browser

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

# Downloading Stuff

ohh, those are all relative
so if I had a playlist of all the .ts links, I could put the file back together again
wow
all of the files in the 
/tsfiles/
compartment

https://stackoverflow.com/questions/22188332/download-ts-files-from-video-stream
https://www.google.com/search?client=safari&rls=en&q=set+request+headers+python&ie=UTF-8&oe=UTF-8

# Plan of Attack
1. extract video.m3u8 link 
2. use RegEx to convert to 1080.m3u8 link 
3. get 1080.m3u8 file 
4. extract .ts links
5. get .ts files and store in folder
6. use converter to put string .ts files together OR use VLC to play them