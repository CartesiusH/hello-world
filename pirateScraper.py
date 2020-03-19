from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://ww7.123moviesfree.sc/season/you-season-1/watching.html/?episode=8912')

episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')

for item in episodes:
    print('{:<50} {:<50}'.format(item.get_attribute('innerHTML'), item.get_attribute('data-strvid')))

    
driver.close()

