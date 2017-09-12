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

url = 'http://centrebet.com/#Racing/67193770'

browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# find all name and place elements
# count name and place elements
# subtract crossed out names
# check if num places = 2*name or 4*names

tempNameElement = browser.find_elements_by_class_name('padLeft10')
nameElement = tempNameElement[2::3]

tempPlaceElement = browser.find_elements_by_class_name('txtOdds')

numNames = 0

for elem in nameElement:
	var = elem.find_element_by_xpath('..')
	var2 = var.get_attribute('class')
	if var2 == 'left txtWht10':
		numNames = numNames + 1
print(numNames)
numPlaces = 0
for elem in tempPlaceElement:
	numPlaces = numPlaces + 1
print(numPlaces)	
if numPlaces == (2 * numNames):
	placeElement = tempPlaceElement[1::2]
elif numPlaces == (4 * numNames):
	placeElement = tempPlaceElement[2::4]
else:
	placeElement = tempPlaceElement[2::4] # CHANGE THIS; it will lead to undefined behaviour


length = numNames
print(length)
i = 0
j = 0
while i < length:
	var = nameElement[i].find_element_by_xpath('..')
	var2 = var.get_attribute('class')

	if var2 == 'left txtWht10':
		print(nameElement[i].text)
		print(placeElement[j].text)
		i = i + 1
		j = j + 1
	else:
		length = length + 1
		i = i + 1


