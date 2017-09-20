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

# URL to TAB race of interest
url = 'https://www.tab.com.au/racing/2017-09-20/WARWICK-FARM/WFM/R/3'

# open that URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# xpaths to horse names
horseName1_tab = '/html/body/ui-view/main/div[1]/ui-view/div/ui-view/div[3]/div[2]/race-runners/div/div[2]/div[2]/div['
horseName2_tab = ']/div[2]/div/div/div'

# xpaths to headers - win, place etc.
headerName1_tab = '/html/body/ui-view/main/div[1]/ui-view/div/ui-view/div[3]/div[2]/race-runners/div/div[2]/div[1]/div[2]/div['
headerName2_tab = ']'

# xpaths to place odds
placeName1_tab = '/html/body/ui-view/main/div[1]/ui-view/div/ui-view/div[3]/div[2]/race-runners/div/div[2]/div[2]/div['
placeName2_tab = ']/div['
placeName3_tab = ']/animate-odds-change/div/div'

time.sleep(10)

# find which column fixed place odds are in
i = 1
j = 0
while j == 0:
	headerName_tab = headerName1_tab + str(i) + headerName2_tab
	var = browser.find_element_by_xpath(headerName_tab).get_attribute('textContent')
	if var.strip() == 'Place':
		columnNumber_tab = i
		j = 1
	else:
		i = i + 1
		
# find number of horses
num_tab = browser.find_elements_by_class_name('runner-name-wrapper')
numHorses_tab = len(num_tab)

# MAKE SURE fixed place odds are in column 7
i = 1
while i <= numHorses_tab:
	horseName_tab = horseName1_tab + str(i) + horseName2_tab
	placeName_tab = placeName1_tab + str(i) + placeName2_tab + str(columnNumber_tab) + placeName3_tab
	nameElement_tab = browser.find_element_by_xpath(horseName_tab)
	placeElement_tab = browser.find_element_by_xpath(placeName_tab).get_attribute('textContent')
	if placeElement_tab != 'SCR':
		var = (nameElement_tab.text).split('(')
		print(var[0])
		print(placeElement_tab)
	i = i + 1
