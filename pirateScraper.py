from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ww7.123moviesfree.sc/season/you-season-1/watching.html/?episode=8912')


elem = driver.find_elements_by_id('Episode 1')
print(elem.get_attribute('outerHTML'))
#print(elem.get_attribute('src'))


'''
PROJECT PLAN
goal: given show name, episode number and season, download episode
steps:
#1 get all episodes
    - a tags direct child of div with les-content class
    - ata-strvid attribute
    - data server attribute
    - by link text
#2 determine which one is the episode we want
    - sort through title attributes
#3 download that epiosde 
    - using lr download thing?
or start with #2? 


for element in elem:
    print element.get_attribute('src')
    print element.get_attribute('class') 
'''

driver.close()

'''
Resources
Selenium Docs
https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text

https://stackoverflow.com/questions/51082130/getting-empty-src-while-scraping/51088253
https://stackoverflow.com/questions/52521456/empty-src-attribute-returned-with-selenium-on-python

'''