# Enter show's name and season number to get show's intro page
print('Enter show\'s name:')
name = input().lower()
print('Enter season number:')
number = input()

base = 'https://ww7.123moviesfree.sc/season/{show}-season-{season}/'
introPage = base.format(show=name,season=number)

# Get episode page url from intro page
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(introPage)

playButton = driver.find_element_by_xpath('//a[@class="thumb mvi-cover"]')
episodePage = (playButton.get_attribute('href'))
driver.get(episodePage)

# Get all episodes by data-Ssrver attribute, then print episode name and video URL
episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')
for item in episodes:
    name = item.get_attribute('innerHTML')
    url = item.get_attribute('data-strvid') 
    print('{:<50} {:<50}'.format(name, url))

driver.close()

'''
Works For: You,

data-server="1" --> data-strvid
data-server="10" --> data-drive
'''

