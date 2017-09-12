from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy
import datetime
import time

# open phantomjs and hide it from the host site
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
  "(KHTML, like Gecko) Chrome/15.0.87")
path_to_phantomjs = 'C:/Python34/Scripts/phantomjs.exe' # path where phantomjs executable file is located
browser = webdriver.PhantomJS(executable_path = path_to_phantomjs, desired_capabilities = dcap)

# specify the path where chromedriver executable file is located
#path_to_chromedriver = 'C:/Python34/Scripts/chromedriver_win32/chromedriver.exe' # change path as needed
#browser = webdriver.Chrome(executable_path = path_to_chromedriver)

# URL to Betfair race
urlBetfair = 'https://www.betfair.com.au/exchange/plus/horse-racing/market/1.134102998'

# get xpaths from Betfair

# xpaths for horse name
horseName1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

horseName2_betfair = ']/td[1]/div/div[2]/mv-runner-info/div/div/div[3]/h3'

# xpaths for lay multipliers
layMultiplier1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

layMultiplier2_betfair = ']/td[5]/button/div/span[1]'

# open Betfair URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(urlBetfair)

browser.implicitly_wait(30)

number = browser.find_elements_by_class_name('bet-button-price')
numHorses = int(len(number) / 6)

time.sleep(10)

for num in range(1,numHorses+1):
	# concatenate xpaths
	horseName_betfair = horseName1_betfair + str(num) + horseName2_betfair
	# backMultiplier = backMultiplier1 + str(num) + backMultiplier2
	layMultiplier_betfair = layMultiplier1_betfair + str(num) + layMultiplier2_betfair
	
	# locate data element and place into array
	try:
		nameElement = browser.find_element_by_xpath(horseName_betfair)
		print(nameElement.text)
	except:
		print("-100")
	
	try:
		layElement = browser.find_element_by_xpath(layMultiplier_betfair)
		print(layElement.text)
	except:
		print("-100")
	



















