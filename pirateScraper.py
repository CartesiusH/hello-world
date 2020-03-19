
# Enter show's name and season number to get show's intro page
print('Show Name:', end=' ')
name = input().lower().replace(' ','-')
print('Season #:', end=' ')
season = input()

base = 'https://ww7.123moviesfree.sc/season/{name}-season-{season}/'
introPage = base.format(name=name,season=season)

# Get episode page url from intro page
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(introPage)

playButton = driver.find_element_by_xpath('//a[@class="thumb mvi-cover"]')
episodePage = (playButton.get_attribute('href'))
driver.get(episodePage)

data = []

# Get all episodes by data-server attribute, then print (and store) episode name and video URL
#Try data-server 1
episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')
for item in episodes:
    name = item.get_attribute('innerHTML')
    url = item.get_attribute('data-strvid')
    if url != None: 
        print('{name:<80} {url:<80}'.format(name=name, url=url).rstrip())
        data.append({'name':name,'url':url})

#If not, try data-server 2
if episodes == []:
    episodes = driver.find_elements_by_xpath('//a[@data-server="10"]')
    for item in episodes:
        name = item.get_attribute('innerHTML')
        url = item.get_attribute('data-drive')
        if url != None: 
            print('{:<50} {:<50}'.format(name, url).rstrip())
            data.append({'name':name,'url':url})

driver.close()



# Allow download option
import re
print('Download Episodes?')
numbers = re.findall('\d', input()) 

spacer=''
downloadList = []
for item in data: # For each episode, extract the episode number (using recorded data)
    epNum = re.findall('\d', item['name'])
    epNum = spacer.join(epNum)
    for number in numbers: # Check if episode number is one user mentioned
        if epNum == number:
            downloadList.append(item['url']) 

