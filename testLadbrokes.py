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

# URL to ladbrokes race of interest
url = 'https://www.ladbrokes.com.au/racing/horses/geelong/38941020-mdn-plate/'

# open that URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# get names of horses
test = browser.find_elements_by_class_name('competitor-name')

# get place odds
# get xpaths to place odds
paths = []
# finds all bet options (win, place etc.)
test3 = browser.find_elements_by_class_name('quickbet')
time.sleep(5)
i = 0
for elem in test3:
	var = elem.get_attribute('data-bettype')
	if var == 'place':
		var2 = elem.get_attribute('data-betspecial')
		if var2 is None:
			var3 = elem.find_elements_by_xpath(".//*")
			for elem2 in var3:
				if elem2.text != "":
					print(test[i].text)
					print(elem2.text)
				i = i + 1
	








