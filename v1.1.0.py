from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy
import datetime
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
     "(KHTML, like Gecko) Chrome/15.0.87")
path_to_phantomjs = 'C:/Python34/Scripts/phantomjs.exe' # change path as needed
browser = webdriver.PhantomJS(executable_path = path_to_phantomjs, desired_capabilities = dcap)

# specify the path where chromedriver executable file is located
#path_to_chromedriver = 'C:/Python34/Scripts/chromedriver_win32/chromedriver.exe' # change path as needed
#browser = webdriver.Chrome(executable_path = path_to_chromedriver)

# open text files for data storage
betfairFile = open('C:/Users/Charith/Desktop/testBetFair.txt', 'w')
williamHillFile = open('C:/Users/Charith/Desktop/testWilliamHill.txt', 'w')

# URL to Betfair race
urlBetfair = 'https://www.betfair.com.au/exchange/plus/horse-racing/market/1.134052501'

# URL to William Hill race
urlWilliamHill = 'https://www.williamhill.com.au/horse-racing/67167516/casterton-2'


# -------------------------------------------------------------
# get CSS selectors from Betfair

# CSS selectors for horse name
horseName1_betfair = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

horseName2_betfair = ') > td.new-runner-info > div > div.runner-data-container > mv-runner-info > div > div > div.name > h3'

# # CSS selectors for back multipliers
# backMultiplier1_betfair = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

# backMultiplier2_betfair = ') > td.bet-buttons.back-cell.last-back-cell > button > div > span.bet-button-price'

# CSS selectors for lay multipliers
layMultiplier1_betfair = '#main-wrapper > div > div.scrollable-panes-height-taker > div > div.page-content.nested-scrollable-pane-parent > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper > bf-marketview-runners-list.runners-list-unpinned > div > div > div > table > tbody > tr:nth-child('

layMultiplier2_betfair = ') > td.bet-buttons.lay-cell.first-lay-cell > button > div > span.bet-button-price'

# -------------------------------------------------------------
# get CSS selectors from William Hill

# CSS selectors for horse names
horseName1_williamHill = '#app > div > div > div.App_contentContainer_3od > div > div > div.TilesLayout_contentContainer_2p5 > div > div > div.RaceCard_layout_2Wt > div.RaceCardList_root_3Mp > div:nth-child(2) > div:nth-child('

horseName2_williamHill = ') > div.RaceCardList_runner_2ii > div > div.Runner_competitor_2Ui > strong'

# CSS selectors for place multipliers
placeMultiplier1_williamHill = '#app > div > div > div.App_contentContainer_3od > div > div > div.TilesLayout_contentContainer_2p5 > div > div > div.RaceCard_layout_2Wt > div.RaceCardList_root_3Mp > div:nth-child(2) > div:nth-child('

placeMultiplier2_williamHill = ') > div.RaceCardList_bodyRight_29m.RaceCardList_gridRight_29v > div.RaceCardList_pane_27j.RaceCardList_paneOpen_3Qb > div.RaceCardList_buttonPair_2ga.RaceCardList_blueBackground_12c > div > button:nth-child(2) > span.BetButton_display_3ty'

# -------------------------------------------------------------
# open Betfair URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.get(urlBetfair)

browser.implicitly_wait(10)

# open William Hill URL
browser.execute_script("window.open('about:blank', 'tab2');")
browser.get(urlWilliamHill)

startTime = datetime.datetime.strptime('Sep 10 2017  12:20', '%b %d %Y %H:%M')

# get current time
currentTime = datetime.datetime.now()

currentTab = 'tab2'

while currentTime < (startTime - datetime.timedelta(minutes=1)):
	#sleep for one second
	time.sleep(1)
	
	if currentTab == 'tab1': # looking at the Betfair page
		for num in range(1,9):
			# concatenate CSS selectors
			horseName_betfair = horseName1_betfair + str(num) + horseName2_betfair
			# backMultiplier = backMultiplier1 + str(num) + backMultiplier2
			layMultiplier_betfair = layMultiplier1_betfair + str(num) + layMultiplier2_betfair
			
			# locate data element and place into array
			try:
				nameElement = browser.find_element_by_css_selector(horseName_betfair)
				betfairFile.write(nameElement.text + ',')
			except InvalidElementStateException:
				betfairFile.write("Exception thrown" + ',')
			

			# backElement = browser.find_element_by_css_selector(backMultiplier)
			# file.write(backElement.text + ',')

			layElement = browser.find_element_by_css_selector(layMultiplier_betfair)
			betfairFile.write(layElement.text + ',')
			
			currentTime = datetime.datetime.now()
			stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
			betfairFile.write(stringTime + '\n')
			
		currentTab = 'tab2'
		browser.switch_to.window(currentTab)
			
	else: # looking at the William Hill page
		for num in range(1,16,2):
			# print horse name
			horseName_williamHill = horseName1_williamHill + str(num) + horseName2_williamHill
			nameElement = browser.find_element_by_css_selector(horseName_williamHill)
			nameElement = nameElement.text
			name1 = nameElement.split('.')
			name2 = name1[1].split('(')
			williamHillFile.write(name2[0].strip() + ',')
			
			# print horse place multipler
			placeMultiplier_williamHill = placeMultiplier1_williamHill + str(num) + placeMultiplier1_williamHill
			placeElement = browser.find_element_by_css_selector(placeMultiplier_williamHill)
			williamHillFile.write(placeElement.text + ',')
	
			# print current time
			currentTime = datetime.datetime.now()
			stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
			williamHillFile.write(stringTime + '\n')
	
		currentTab = 'tab1'
		browser.switch_to.window(currentTab)
		
# close file handle	
betfairFile.close()
williamHillFile.close()
















