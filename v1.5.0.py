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

configFileLocation = 'C:/Users/Charith/Desktop/Configuration File.txt'
with open(configFileLocation) as f:
    configList = f.read().splitlines()

betfairFileLocation = configList[7]
williamHillFileLocation = configList[11]
centrebetFileLocation = configList[15]
unibetFileLocation = configList[19]

betfairFile = open(betfairFileLocation, 'w')
williamHillFile = open(williamHillFileLocation, 'w')
centrebetFile = open(centrebetFileLocation, 'w')
unibetFile = open(unibetFileLocation, 'w')

# URL to Betfair race
urlBetfair = configList[5]

# URL to William Hill race
urlWilliamHill = configList[9]

# URL to centrebet race
urlCentrebet = configList[13]

# URL to unibet race
urlUnibet = configList[17]

# -------------------------------------------------------------
# get xpaths from Betfair

# xpaths for horse name
horseName1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/'
'bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

horseName2_betfair = ']/td[1]/div/div[2]/mv-runner-info/div/div/div[3]/h3'

# xpaths for lay multipliers
layMultiplier1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/'
'bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

layMultiplier2_betfair = ']/td[5]/button/div/span[1]'

# -------------------------------------------------------------
# get xpaths from William Hill

# xpaths for horse names
horseName1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/div['

horseName2_williamHill = ']/div[1]/div/div[2]/strong'

# xpaths for place multipliers
placeMultiplier1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/div['

placeMultiplier2_williamHill = ']/div[2]/div[1]/div[3]/div/button[2]/span[2]'

# -------------------------------------------------------------
# get xpaths from Unibet

# xpaths to header names
headerName1_unibet = '//*[@id="center-column"]/div/div/div/div['
headerName2_unibet = ']/table/thead/tr[2]/th['
headerName3_unibet = ']'

# xpaths to place multipliers	
placeName1_unibet = '//*[@id="center-column"]/div/div/div/div['
placeName2_unibet = ']/table/tbody/tr['
placeName3_unibet = ']/td['
placeName4_unibet = ']/div/button'

# -------------------------------------------------------------
# open Betfair URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(urlBetfair)

browser.implicitly_wait(30)

# open William Hill URL
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window(browser.window_handles[1])
browser.get(urlWilliamHill)

browser.switch_to.window(browser.window_handles[0])

# open centrebet URL
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window(browser.window_handles[2])
browser.get(urlCentrebet)

browser.switch_to.window(browser.window_handles[0])

# open unibet URL
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window(browser.window_handles[3])
browser.get(urlUnibet)

browser.switch_to.window(browser.window_handles[0])

startTimeString = configList[1]
startTime = datetime.datetime.strptime(startTimeString, '%b %d %Y %H:%M')

# get current time
currentTime = datetime.datetime.now()

handle = 0

while currentTime < (startTime - datetime.timedelta(minutes=1)):

	if handle == 0:
		handle = 1
		browser.switch_to.window(browser.window_handles[1])
	elif handle == 1:
		handle = 2
		browser.switch_to.window(browser.window_handles[2])
	elif handle == 2:
		handle = 3
		browser.switch_to.window(browser.window_handles[3])
	else:
		handle = 0
		browser.switch_to.window(browser.window_handles[0])
	
	if handle == 0: # looking at the Betfair page
		print('betfair')
		number = browser.find_elements_by_class_name('bet-button-price')
		numHorses = int(len(number) / 6)
		for num in range(1,numHorses+1):
			# concatenate xpaths
			horseName_betfair = horseName1_betfair + str(num) + horseName2_betfair
			layMultiplier_betfair = layMultiplier1_betfair + str(num) + layMultiplier2_betfair
			
			# locate data element and place into array
			try:
				nameElement = browser.find_element_by_xpath(horseName_betfair)
				betfairFile.write(nameElement.text + ',')
			except:
				betfairFile.write("Error" + ',')
			
			try:
				layElement = browser.find_element_by_xpath(layMultiplier_betfair)
				betfairFile.write(layElement.text + ',')
			except:
				betfairFile.write("Error" + ',')
				
			currentTime = datetime.datetime.now()
			stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
			betfairFile.write(stringTime + '\n')
			
	elif handle == 1: # looking at the William Hill page
		print('william hill')
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
				williamHillFile.write(name2[0].strip() + ',')
			except:
				williamHillFile.write("Error" + ',')

			# print horse place multipler
			placeMultiplier_williamHill = placeMultiplier1_williamHill + str(num) + placeMultiplier2_williamHill
			try:
				placeElement = browser.find_element_by_xpath(placeMultiplier_williamHill)
				williamHillFile.write(placeElement.text + ',')
			except:
				williamHillFile.write("Error" + ',')
				
			currentTime = datetime.datetime.now()
			stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
			williamHillFile.write(stringTime + '\n')
			
	elif handle == 2: # looking at Centrebet page
		print('centrebet')
		try:
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
					centrebetFile.write(nameElement[i].text + ',')
					centrebetFile.write(placeElement[j].text + ',')
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					centrebetFile.write(stringTime + '\n')
					i = i + 1
					j = j + 1
				else:
					length = length + 1
					i = i + 1
		except:
			centrebetFile.write('Error,' + 'Error,' + 'Error\n')
	else: # looking at the Unibet page
		print('unibet')
		
		# switch to the frame where the data is in
		frame = browser.find_element_by_css_selector('#uarc')
		browser.switch_to.frame(frame)
	
		# number of table subheaders - eg: fixed, mid tote etc.
		i = 0
		j = 2
		while i == 0:
			try:
				headerName_unibet = headerName1_unibet + str(j) + headerName2_unibet + '1' + headerName3_unibet
				var = browser.find_element_by_xpath(headerName_unibet)
				i = 1
				numSubheaders = j
			except:
				j = j + 1

		# 'k' will give the column in which place odds are located
		i = 0
		k = 3
		while i == 0:
			headerName_unibet = headerName1_unibet + str(j) + headerName2_unibet + str(k) + headerName3_unibet
			var = browser.find_element_by_xpath(headerName_unibet)

			if var.text == "Fixed":
				i = 1
			else:
				k = k + 1	

		col = k + 5
				
		# find number of horses
		tempNameElement = browser.find_elements_by_class_name('event-runner__name')
		length = len(tempNameElement)

		i = 1
		j = 0
		while i <= length:
			placeName_unibet = placeName1_unibet + str(numSubheaders) + placeName2_unibet + str(i) + placeName3_unibet + str(k + 5) + placeName4_unibet
			try:
				placeElement_unibet = browser.find_element_by_xpath(placeName_unibet)
				unibetFile.write(tempNameElement[j].text + ',')
				unibetFile.write(placeElement_unibet.text + ',')
				currentTime = datetime.datetime.now()
				stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
				unibetFile.write(stringTime + '\n')
				j = j + 1
			except:
				length = length + 1
			
			i = i + 1
	
		
# close file handle	
betfairFile.close()
williamHillFile.close()
centrebetFile.close()
unibetFile.close()














