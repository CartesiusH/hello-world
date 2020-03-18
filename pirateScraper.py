from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ww3.fmovie.sc/free/you-season-1/watching.html/?episode=10565')

elem = driver.find_element_by_id('iframe-embed')
print(elem.get_attribute('src'))


'''
for element in elem:
    print element.get_attribute('src')
    print element.get_attribute('class') 
'''

driver.close()

'''
Resources
https://stackoverflow.com/questions/51082130/getting-empty-src-while-scraping/51088253
https://stackoverflow.com/questions/52521456/empty-src-attribute-returned-with-selenium-on-python

'''