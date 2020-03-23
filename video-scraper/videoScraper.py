def getInput():
    print('Show Name:', end=' ')
    raw_name = input()
    name = raw_name.lower().replace(' ','-')
    print('Season #:', end=' ')
    season = input()

    return raw_name, name, season


def getEpisodePage(name, season):
    # Get intro page 
    base = 'https://ww7.123moviesfree.sc/season/{name}-season-{season}/'
    introPage = base.format(name=name,season=season)
    driver.get(introPage)

    # Get episode page
    playButton = driver.find_element_by_xpath('//a[@class="thumb mvi-cover"]')
    episodePage = (playButton.get_attribute('href'))

    return episodePage


def getEpisodeLinks(episodePage):
    # Get all episodes by data-server attribute, then print (and store) episode name and video URL
    driver.get(episodePage)
    episodeLinks = []

    # Try data-server 1
    episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')
    for item in episodes:
        name = item.get_attribute('innerHTML')
        url = item.get_attribute('data-strvid')
        if url != None: 
            episodeLinks.append({'name':name,'url':url})

    # If not, try data-server 2
    if episodes == []:
        episodes = driver.find_elements_by_xpath('//a[@data-server="10"]')
        for item in episodes:
            name = item.get_attribute('innerHTML')
            url = item.get_attribute('data-drive')
            if url != None: 
                episodeLinks.append({'name':name,'url':url})
    
    # Print episode links
    for item in episodeLinks:
        print('{name:<80} {url:<80}'.format(name=item['name'], url=item['url']).rstrip())

    return episodeLinks

def selectEpisodes(episodeLinks):
    import re
    print('Download Episodes?')
    numbers = re.findall('\d', input()) 

    spacer=''
    downloadList = []
    numList = []

    for item in episodeLinks: # For each episode, extract the episode number (using recorded data)
        epNum = re.findall('\d', item['name'])
        epNum = spacer.join(epNum)
        for number in numbers: # Check if episode number is one user mentioned
            if epNum == number:
                downloadList.append(item['url']) 
                numList.append(number)

    return downloadList, numList


def getFileLinks(episode):
    # Get 1080.m3u8 link
    driver = webdriver.Safari()
    driver.get(episode)

    video_m3u8 = driver.find_element_by_tag_name('video').get_attribute('src')
    final_m3u8 = video_m3u8.replace('video.m3u8','1080.m3u8')

    driver.close()

    # Get m3u8 file
    global headers
    headers = {
        'Accept':'*/*',
        'Connection':'keep-alive',
        'Host':'shockwave.streamvid.co',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
        'Accept-Language':'en-us',
        'Referer': episode,
        'Accept-Encoding':'gzip'
    }
    playlist = requests.get(final_m3u8, headers=headers).content.decode('utf-8').split()

    # Extract .ts links
    tslinks = []
    for line in playlist:
        if not line.lstrip().startswith('#'):
            tslinks.append('https://shockwave.streamvid.co'+line)
    
    return tslinks

def makeDirectory(raw_name, season, episodeNumber):
    import os
    directory = raw_name + '_s' + season + 'e' + episodeNumber
    parent_dir = '/Users/mica/Movies/'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    return path

def downloadTsFile(link, path):  
    time.sleep(1)
    tsfile = requests.get(link, headers=headers)

    file_name = str(counter)
    filePath = path + '/' + file_name

    with open(filePath,'wb') as f:
        f.write(tsfile.content)

def createJoinFile(path):
    import os
    from natsort import natsorted
    files = natsorted(os.listdir(path))
    
    join_file = path + '.txt'
    with open(join_file,'w') as f:
        for file in files:
            f.write('file \''+ path + '/' + file + '\' \n') 

    return join_file



# use  ffmpeg -f concat -safe 0 -i join.txt -c copy output.mp4

'''
# Get Episode Links of Choice
raw_name, name, season = getInput()
from selenium import webdriver

driver = webdriver.Chrome()
episodePage = getEpisodePage(name, season)
episodeLinks = getEpisodeLinks(episodePage)
driver.close()

# Download Episodes of Choice
downloadList, numList = selectEpisodes(episodeLinks)
for episode in downloadList:
    import requests
    tslinks = getFileLinks(episode)
    path = makeDirectory(raw_name, season, numList[downloadList.index(episode)])

    import time
    counter = 0
    print(len(tslinks),' files to install.')
    headers['Accept-Encoding'] = 'idenity'

    for link in tslinks:
        counter += 1
        try:
            downloadTsFile(link, path)
        except RemoteDisconnected: # This part not working apparently
            print('Remote disconnected, waiting 5 seconds and trying again.')
            time.sleep(5)
            downloadTsFile(link, path)

    join_file = createJoinFile(path)
'''

path = '/Users/mica/Movies/YOU_s1e6'
createJoinFile(path)
    

'''
Fix double import 
Refactor some more
Need better way to refactor, should read Clean Code
'''
