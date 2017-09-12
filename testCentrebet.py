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

url = 'http://centrebet.com/#Racing/67193775'

browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

tempNameElement = browser.find_elements_by_class_name('padLeft10')
nameElement = tempNameElement[2::3]

placeElement = browser.find_elements_by_xpath('//*[starts-with(@id, "divFPP")]')

i = 0
j = 0
length = len(placeElement)
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
