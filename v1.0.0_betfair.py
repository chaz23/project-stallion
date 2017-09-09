from selenium import webdriver
import numpy
import datetime
import time

# specify the path where chromedriver executable file is located
path_to_chromedriver = 'C:/Python34/Scripts/chromedriver_win32/chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

# URL to betfair race of interest
url = 'https://www.betfair.com.au/exchange/plus/horse-racing/market/1.134009803'

# open that URL
browser.get(url)

browser.implicitly_wait(10)

# get CSS selector for horse name
horseName1 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

horseName2 = ') > td.new-runner-info > div > div.runner-data-container > mv-runner-info > div > div > div.name > h3'

# get CSS selector for back multipliers
backMultiplier1 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

backMultiplier2 = ') > td.bet-buttons.back-cell.last-back-cell > button > div > span.bet-button-price'

#get CSS selector for lay multipliers
layMultiplier1 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

layMultiplier2 = ') > td.bet-buttons.lay-cell.first-lay-cell > button > div > span.bet-button-price'

# open text file for data storage
file = open('C:/Users/Charith/Desktop/test.txt', 'w')

# get race start time
#raceStartTime = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div:nth-child(1) > div > div > div > div > div.event-header > div > span.venue-name'

#startTimeElement = browser.find_element_by_css_selector(raceStartTime)
#startTime = (startTimeElement.text).split(' ', 1)[0]
#startTime = datetime.datetime.strptime(startTime, '%H:%M')

startTime = datetime.datetime.strptime('Sep 9 2017  22:55', '%b %d %Y %H:%M')

# get current time
currentTime = datetime.datetime.now()

while currentTime < (startTime - datetime.timedelta(minutes=1)):

	# put data into matrix
	for num in range(1,9):
		# concatenate CSS selectors
		horseName = horseName1 + str(num) + horseName2
		backMultiplier = backMultiplier1 + str(num) + backMultiplier2
		layMultiplier = layMultiplier1 + str(num) + layMultiplier2
		
		# locate data element and place into array
		nameElement = browser.find_element_by_css_selector(horseName)
		print(nameElement.text)
		file.write(nameElement.text + ',')

		backElement = browser.find_element_by_css_selector(backMultiplier)
		print(backElement.text)
		file.write(backElement.text + ',')

		layElement = browser.find_element_by_css_selector(layMultiplier)
		print(layElement.text)
		file.write(layElement.text + ',')
		
		#sleep for one second
		time.sleep(1)
		
		currentTime = datetime.datetime.now()
		stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
		file.write(stringTime + '\n')

# close file handle	
file.close()
