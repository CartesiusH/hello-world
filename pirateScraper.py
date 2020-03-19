# Enter show's name and season number to get show's intro page
print('Enter show\'s name:')
name = input().lower().replace(' ','-')
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

# Get all episodes by data-server attribute, then print episode name and video URL
#Try data-server 1
episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')
for item in episodes:
    name = item.get_attribute('innerHTML')
    url = item.get_attribute('data-strvid')
    if url != None: 
        print('{name:<80} {url:<80}'.format(name=name, url=url).rstrip())

#If not, try data-server 2
if episodes == []:
    episodes = driver.find_elements_by_xpath('//a[@data-server="10"]')
    for item in episodes:
        name = item.get_attribute('innerHTML')
        url = item.get_attribute('data-drive')
        if url != None: 
            print('{:<50} {:<50}'.format(name, url).rstrip())

driver.close()
