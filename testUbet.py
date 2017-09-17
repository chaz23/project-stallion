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

# URL to ubet race of interest
url = 'https://ubet.com/racing/horse-racing/Geelong-VR/Race-7/Win?Date=20170917'

# open that URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# check the ubet column header to ensure it is fixed place odds
check = browser.find_element_by_css_selector('#page-container > racing-container > div > div > single-leg-container > div > div.race-single-leg-grid > div > div > div.runner-offer-header > div.fixed-price-header > p:nth-child(2)').get_attribute('textContent')

assert check.strip() == 'F Place'

# css selectors to ubet horse names
horseName1_ubet = '#page-container > racing-container > div > div > single-leg-container > div > div.race-single-leg-grid > div > ul > li:nth-child('

horseName2_ubet = ') > ubet-race-single-leg-grid > ul > li > div > div:nth-child(1) > div > div > div > div.ubet-racing-race-runner-information > ubet-racing-race-runner-information > div > div.runner-details > div.runner-name > div > span.n1.not-harness'

# get place odds and number of horses
placeElement_ubet = browser.find_elements_by_class_name('odds')
placeElement_ubet = placeElement_ubet[3::4]
numHorses_ubet = len(placeElement_ubet)

# find which horses are scratched
i = 1
j = 1
horseNameList = []
while i <= numHorses_ubet:
	try:
		horseName_ubet = horseName1_ubet + str(j) + horseName2_ubet
		nameElement_ubet = browser.find_element_by_css_selector(horseName_ubet)
		horseNameList.insert(i-1,j)
		i = i + 1
	except:
		pass
	j = j + 1
	
print(horseNameList)

i = 0
for elem in horseNameList:
	horseName_ubet = horseName1_ubet + str(elem) + horseName2_ubet
	nameElement_ubet = browser.find_element_by_css_selector(horseName_ubet)
	print(nameElement_ubet.text)
	print(placeElement_ubet[i].text)
	i = i + 1
	




















