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

url = 'https://www.unibet.com.au/racing#/event/1594207/win?_k=e9qf5w'
url2 = 'https://www.betfair.com.au/exchange/plus/horse-racing/market/1.134188929?nodeId=28385200'

browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# switch to the frame where the data is in
frame = browser.find_element_by_css_selector('#uarc')
browser.switch_to.frame(frame)	

# xpaths to header names
headerName1 = '//*[@id="center-column"]/div/div/div/div['
headerName2 = ']/table/thead/tr[2]/th['
headerName3 = ']'

# xpaths to horse names
horseName1 = '//*[@id="center-column"]/div/div/div/div[3]/table/tbody/tr['
horseName2 = ']/td[3]/div/div/span/a'

# xpaths to place multipliers	
placeName1 = '//*[@id="center-column"]/div/div/div/div['
placeName2 = ']/table/tbody/tr['
placeName3 = ']/td['
placeName4 = ']/div/button'

# number of table subheaders - eg: fixed, mid tote etc.
i = 0
j = 2
while i == 0:
	try:
		headerName = headerName1 + str(j) + headerName2 + '1' + headerName3
		var = browser.find_element_by_xpath(headerName)
		i = 1
		numSubheaders = j
	except:
		j = j + 1

# 'k' will give the column in which place odds are located
i = 0
k = 3
while i == 0:
	headerName = headerName1 + str(j) + headerName2 + str(k) + headerName3
	var = browser.find_element_by_xpath(headerName)

	if var.text == "Fixed":
		i = 1
	else:
		k = k + 1	

col = k + 5
		
# find number of horses
tempNameElement = browser.find_elements_by_class_name('event-runner__name')
length = len(tempNameElement)

# find which unibet horses are scratched
i = 1
j = 0
count = length
numList = []
while i <= count:
	horseName = horseName1 + str(i) + horseName2
	nameElement = browser.find_element_by_xpath(horseName)
	var = nameElement.get_attribute('class')
	if var == 'event-runner__name':
		numList.insert(j,i)
		j = j + 1
	else:
		count = count + 1
	i = i + 1
	
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window(browser.window_handles[1])
browser.get(url2)

browser.switch_to.window(browser.window_handles[0])
frame = browser.find_element_by_css_selector('#uarc')
browser.switch_to.frame(frame)

	
j = 0
for i in numList:
	placeName = placeName1 + str(numSubheaders) + placeName2 + str(i) + placeName3 + str(k + 5) + placeName4
	placeElement = browser.find_element_by_xpath(placeName)
	print(tempNameElement[j].text)
	print(placeElement.text)
	j = j + 1


