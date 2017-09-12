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

# URL to betfair race of interest
url = 'https://www.williamhill.com.au/horse-racing/67193770/tamworth-1'

# open that URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# xpaths for horse names
horseName1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[4]/div[2]/div['

horseName2_williamHill = ']/div[1]/div/div[2]/strong'

# xpaths for place multipliers
placeMultiplier1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[4]/div[2]/div['

placeMultiplier2_williamHill = ']/div[2]/div[1]/div[3]/div/button[2]/span[2]'

numHorses = browser.find_elements_by_class_name('Runner_competitor_2Ui')
length = len(numHorses)

for num in range(1, 2 * length, 2):
	# print horse name
	horseName_williamHill = horseName1_williamHill + str(num) + horseName2_williamHill
	try:
		nameElement = browser.find_element_by_xpath(horseName_williamHill)
		nameElement = nameElement.text
		name1 = nameElement.split('.')
		name2 = name1[1].split('(')
		print(name2[0].strip())
	except:
		print("-100")

	# print horse place multipler
	placeMultiplier_williamHill = placeMultiplier1_williamHill + str(num) + placeMultiplier2_williamHill
	try:
		placeElement = browser.find_element_by_xpath(placeMultiplier_williamHill)
		print(placeElement.text)
	except:
		print("-100")

		
		
		
		
		
		