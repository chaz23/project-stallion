from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy
import datetime
import time
import winsound

# function to analyze lay and place multipliers
def analyzePrices(nameList_betfair, priceList_betfair, nameList_williamHill, priceList_williamHill, nameList_centrebet, priceList_centrebet, nameList_unibet, priceList_unibet):
	try:
		# convert names to lowercase
		nameList_betfair = [x.lower() for x in nameList_betfair]
		nameList_williamHill = [x.lower() for x in nameList_williamHill]
		nameList_centrebet = [x.lower() for x in nameList_centrebet]
		nameList_unibet = [x.lower() for x in nameList_unibet]
		
		# removes apostrophes
		nameList_betfair = [x.replace("'","") for x in nameList_betfair]
		nameList_williamHill = [x.replace("'","") for x in nameList_williamHill]
		nameList_centrebet = [x.replace("'","") for x in nameList_centrebet]
		nameList_unibet = [x.replace("'","") for x in nameList_unibet]
		
		namePrice_betfair = [list(a) for a in zip(nameList_betfair, priceList_betfair)]
		namePrice_williamHill = [list(a) for a in zip(nameList_williamHill, priceList_williamHill)]
		namePrice_centrebet = [list(a) for a in zip(nameList_centrebet, priceList_centrebet)]
		namePrice_unibet = [list(a) for a in zip(nameList_unibet, priceList_unibet)]

		# sort back sites according to betfair name order
		namePrice_williamHill.sort(key=lambda x: nameList_betfair.index(x[0]))
		namePrice_centrebet.sort(key=lambda x: nameList_betfair.index(x[0]))
		namePrice_unibet.sort(key=lambda x: nameList_betfair.index(x[0]))
		
		length = len(namePrice_betfair)
		
		duration = 300  # millisecond
		freq = 1000  # Hz
		
		# analyze prices
		i = 0
		while i < length:
			try:
				williamHillDiff = float(namePrice_williamHill[i][1]) - float(namePrice_betfair[i][1])
				centrebetDiff = float(namePrice_centrebet[i][1]) - float(namePrice_betfair[i][1])
				unibetDiff = float(namePrice_unibet[i][1]) - float(namePrice_betfair[i][1])
				
				# alert if opportunity exists
				if williamHillDiff > 0:
					print('Arb on William Hill')
					print('Horse: ' + namePrice_williamHill[i][0])
					winsound.Beep(freq, duration)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					print('Time: ' + stringTime)
				elif centrebetDiff > 0:
					print('Arb on Centrebet')
					print('Horse: ' + namePrice_centrebet[i][0])
					winsound.Beep(freq, duration)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					print('Time: ' + stringTime)
				elif unibetDiff > 0:
					print('Arb on Unibet')
					print('Horse: ' + namePrice_unibet[i][0])
					winsound.Beep(freq, duration)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					print('Time: ' + stringTime)
				
				i = i + 1
			except:
				i = i + 1
	except:
		print('Error while analyzing odds')
	
	return
	

# configuration file location
configFileLocation = 'C:/Users/Charith/Desktop/Configuration File.txt'
with open(configFileLocation) as f:
    configList = f.read().splitlines()

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

# extract parameters from configuration file
betfairFileLocation = configList[5]
williamHillFileLocation = configList[9]
centrebetFileLocation = configList[13]
unibetFileLocation = configList[17]

# create liquidity file
tempBetfairFileLocation = betfairFileLocation.split('_')
betfairLiquidityFileLocation = tempBetfairFileLocation[0] + '_' + tempBetfairFileLocation[1] + ' Liquidity' + '_' + tempBetfairFileLocation[2]

betfairFile = open(betfairFileLocation, 'w')
betfairLiquidityFile = open(betfairLiquidityFileLocation, 'w')
williamHillFile = open(williamHillFileLocation, 'w')
centrebetFile = open(centrebetFileLocation, 'w')
unibetFile = open(unibetFileLocation, 'w')

# URL to Betfair race
urlBetfair = configList[3]

# URL to William Hill race
urlWilliamHill = configList[7]

# URL to centrebet race
urlCentrebet = configList[11]

# URL to unibet race
urlUnibet = configList[15]

# -------------------------------------------------------------
# get xpaths from Betfair

# xpaths for horse name
horseName1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

horseName2_betfair = ']/td[1]/div/div[2]/mv-runner-info/div/div/div[3]/h3'

# xpaths for lay multipliers
layMultiplier1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

layMultiplier2_betfair = ']/td[5]/button/div/span[1]'

# xpaths for liquidity
liquidity1_betfair = '//*[@id="main-wrapper"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr['

liquidity2_betfair = ']/td[5]/button/div/span[2]'

# -------------------------------------------------------------
# get xpaths from William Hill

horseName1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div['

horseName2_williamHill = ']/div[2]/div['

horseName3_williamHill = ']/div[1]/div/div[2]/strong'

# xpaths for place multipliers
placeMultiplier1_williamHill = '//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div['

placeMultiplier2_williamHill = ']/div[2]/div['

placeMultiplier3_williamHill = ']/div[2]/div[1]/div[3]/div/button[2]/span[2]'

# -------------------------------------------------------------
# get xpaths from unibet

# xpaths to header names
headerName1_unibet = '//*[@id="center-column"]/div/div/div/div['
headerName2_unibet = ']/table/thead/tr[2]/th['
headerName3_unibet = ']'

# xpaths to horse names
horseName1_unibet = '//*[@id="center-column"]/div/div/div/div[3]/table/tbody/tr['
horseName2_unibet = ']/td[3]/div/div/span/a'

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

# --------------------------------------------------
# open William Hill URL
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window(browser.window_handles[1])
browser.get(urlWilliamHill)

# xpaths change based on how many multiplier columns are available
try:
	test1 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[3]/div/div[1]')
	williamHillcolumn = 3
except:
	test2 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div/div[1]/div/div/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[3]/div/div[1]')
	williamHillcolumn = 4

browser.switch_to.window(browser.window_handles[0])

# ---------------------------------------------------
# open centrebet URL
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window(browser.window_handles[2])
browser.get(urlCentrebet)

browser.switch_to.window(browser.window_handles[0])

# ---------------------------------------------------
# open unibet URL
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window(browser.window_handles[3])
browser.get(urlUnibet)

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
		numSubheaders_unibet = j
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
tempNameElement_unibet = browser.find_elements_by_class_name('event-runner__name')
length_unibet = len(tempNameElement_unibet)

# find which unibet horses are scratched
i = 1
j = 0
count = length_unibet
numList_unibet = []
while i <= count:
	horseName_unibet = horseName1_unibet + str(i) + horseName2_unibet
	nameElement = browser.find_element_by_xpath(horseName_unibet)
	var = nameElement.get_attribute('class')
	if var == 'event-runner__name':
		numList_unibet.insert(j,i)
		j = j + 1
	else:
		count = count + 1
	i = i + 1

# --------------------------------------------------------

startTimeString = configList[1]
startTime = datetime.datetime.strptime(startTimeString, '%b %d %Y %H:%M')

# get current time
currentTime = datetime.datetime.now()

handle = 3

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
		nameList_betfair = []
		priceList_betfair = []
		for num in range(1,numHorses+1):
			# concatenate xpaths
			horseName_betfair = horseName1_betfair + str(num) + horseName2_betfair
			layMultiplier_betfair = layMultiplier1_betfair + str(num) + layMultiplier2_betfair
			liquidity_betfair = liquidity1_betfair + str(num) + liquidity2_betfair

			# locate data element and place into array
			try:
				nameElement = browser.find_element_by_xpath(horseName_betfair)
				betfairFile.write(((nameElement.text).replace("'","")).lower() + ',')
				betfairLiquidityFile.write(((nameElement.text).replace("'","")).lower() + ',')
				nameList_betfair.insert(num-1,nameElement.text)
			except:
				betfairFile.write("Error" + ',')
				betfairLiquidityFile.write("Error" + ',')
				nameList_betfair.insert(num-1,'Error')
			
			try:
				layElement = browser.find_element_by_xpath(layMultiplier_betfair)
				liquidityElement = browser.find_element_by_xpath(liquidity_betfair)
				betfairFile.write(layElement.text + ',')
				betfairLiquidityFile.write(liquidityElement.text + ',')
				priceList_betfair.insert(num-1,layElement.text)
			except:
				betfairFile.write("Error" + ',')
				betfairLiquidityFile.write("Error" + ',')
				priceList_betfair.insert(num-1,'Error')
				
			currentTime = datetime.datetime.now()
			stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
			betfairFile.write(stringTime + ',')
			betfairFile.write('Betfair\n')
			betfairLiquidityFile.write(stringTime + ',')
			betfairLiquidityFile.write('Betfair Liquidity\n')
			
	elif handle == 1: # looking at the William Hill page
		print('william hill')
		numHorses = browser.find_elements_by_class_name('Runner_competitor_2Ui')
		length = len(numHorses)

		nameList_williamHill = []
		priceList_williamHill = []
		count = 0
		for num in range(1, 2 * length, 2):
			# print horse name and place multiplier
			horseName_williamHill = horseName1_williamHill + str(williamHillcolumn) + horseName2_williamHill + str(num) + horseName3_williamHill
			placeMultiplier_williamHill = placeMultiplier1_williamHill + str(williamHillcolumn) + placeMultiplier2_williamHill + str(num) + placeMultiplier3_williamHill
			try:
				nameElement = browser.find_element_by_xpath(horseName_williamHill)
				placeElement = browser.find_element_by_xpath(placeMultiplier_williamHill)
				nameElement = nameElement.text
				name1 = nameElement.split('.')
				name2 = name1[1].split('(')
				if placeElement.text != 'SCR':
					williamHillFile.write(((name2[0].strip()).replace("'","")).lower() + ',')
					williamHillFile.write(placeElement.text + ',')
					nameList_williamHill.insert(count,name2[0].strip())
					priceList_williamHill.insert(count,placeElement.text)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					williamHillFile.write(stringTime + ',')
					williamHillFile.write('William Hill\n')
					count = count + 1
			except:
				williamHillFile.write("Error,Error,")
				currentTime = datetime.datetime.now()
				stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
				williamHillFile.write(stringTime + ',')
				williamHillFile.write('William Hill\n')
				nameList_williamHill.insert(count,'Error')
				priceList_williamHill.insert(count,'Error')
				count = count + 1						
			
	elif handle == 2: # looking at Centrebet page
		print('centrebet')
		nameList_centrebet = []
		priceList_centrebet = []
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
					centrebetFile.write(((nameElement[i].text).replace("'","")).lower() + ',')
					centrebetFile.write(placeElement[j].text + ',')
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					centrebetFile.write(stringTime + ',')
					centrebetFile.write('Centrebet\n')
					
					nameList_centrebet.insert(j,(nameElement[i].text))
					priceList_centrebet.insert(j,placeElement[j].text)
					i = i + 1
					j = j + 1
				else:
					length = length + 1
					i = i + 1
		except:
			centrebetFile.write('Error,' + 'Error,' + 'Error,' + 'Error\n')
			nameList_centrebet.insert(0,'Error')
			priceList_centrebet.insert(0,'Error')
	
		browser.find_element_by_xpath('//*[@id="main"]/div[2]/h3/a[3]').click()
	
	else: # looking at unibet site
		print('unibet')
		frame = browser.find_element_by_css_selector('#uarc')
		browser.switch_to.frame(frame)
		
		nameList_unibet = []
		priceList_unibet = []
		
		try:
			j = 0
			for i in numList_unibet:
				placeName_unibet = placeName1_unibet + str(numSubheaders_unibet) + placeName2_unibet + str(i) + placeName3_unibet + str(k + 5) + placeName4_unibet
				placeElement = browser.find_element_by_xpath(placeName_unibet)
				unibetFile.write(((tempNameElement_unibet[j].text).replace("'","")).lower() + ',')
				unibetFile.write(placeElement.text + ',')
				
				nameList_unibet.insert(j,(tempNameElement_unibet[j].text))
				priceList_unibet.insert(j,placeElement.text)
				
				currentTime = datetime.datetime.now()
				stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
				unibetFile.write(stringTime + ',')
				unibetFile.write('Unibet\n')
				
				j = j + 1
		except:
			unibetFile.write('Error,' + 'Error,' + 'Error,' + 'Error\n')
			nameList_unibet.insert(0,'Error')
			priceList_unibet.insert(0,'Error')
		
		analyzePrices(nameList_betfair, priceList_betfair, nameList_williamHill, priceList_williamHill, nameList_centrebet, priceList_centrebet, nameList_unibet, priceList_unibet)
	
# close file handle	
betfairFile.close()
betfairLiquidityFile.close()
williamHillFile.close()
centrebetFile.close()
unibetFile.close()