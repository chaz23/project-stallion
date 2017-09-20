from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy
import datetime
import time
import winsound

# function to analyze lay and place multipliers
def analyzePrices(nameList_betfair, priceList_betfair, nameList_ladbrokes, priceList_ladbrokes, nameList_tab, priceList_tab, nameList_ubet, priceList_ubet):
	try:
		# convert names to lowercase
		nameList_betfair = [x.lower() for x in nameList_betfair]
		nameList_ladbrokes = [x.lower() for x in nameList_ladbrokes]
		nameList_tab = [x.lower() for x in nameList_tab]
		nameList_ubet = [x.lower() for x in nameList_ubet]
		
		# removes apostrophes
		nameList_betfair = [x.replace("'","") for x in nameList_betfair]
		nameList_ladbrokes = [x.replace("'","") for x in nameList_ladbrokes]
		nameList_tab = [x.replace("'","") for x in nameList_tab]
		nameList_ubet = [x.replace("'","") for x in nameList_ubet]
		
		namePrice_betfair = [list(a) for a in zip(nameList_betfair, priceList_betfair)]
		namePrice_ladbrokes = [list(a) for a in zip(nameList_ladbrokes, priceList_ladbrokes)]
		namePrice_tab = [list(a) for a in zip(nameList_tab, priceList_tab)]
		namePrice_ubet = [list(a) for a in zip(nameList_ubet, priceList_ubet)]

		# sort back sites according to betfair name order
		namePrice_ladbrokes.sort(key=lambda x: nameList_betfair.index(x[0]))
		namePrice_tab.sort(key=lambda x: nameList_betfair.index(x[0]))
		namePrice_ubet.sort(key=lambda x: nameList_betfair.index(x[0]))
		
		length = len(namePrice_betfair)
		
		duration = 300  # millisecond
		freq = 1000  # Hz
		
		# analyze prices
		i = 0
		while i < length:
			try:
				ladbrokesDiff = float(namePrice_ladbrokes[i][1]) - float(namePrice_betfair[i][1])
				tabDiff = float(namePrice_tab[i][1]) - float(namePrice_betfair[i][1])
				ubetDiff = float(namePrice_ubet[i][1]) - float(namePrice_betfair[i][1])
				
				# alert if opportunity exists
				if ladbrokesDiff > 0:
					print('Arb on Ladbrokes')
					print('Horse: ' + namePrice_ladbrokes[i][0])
					print('Odds: ' + namePrice_ladbrokes[i][1])
					winsound.Beep(freq, duration)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					print('Time: ' + stringTime)
				elif tabDiff > 0:
					print('Arb on TAB')
					print('Horse: ' + namePrice_tab[i][0])
					print('Odds: ' + namePrice_tab[i][1])
					winsound.Beep(freq, duration)
					currentTime = datetime.datetime.now()
					stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
					print('Time: ' + stringTime)
				elif ubetDiff > 0:
					print('Arb on Ubet')
					print('Horse: ' + namePrice_ubet[i][0])
					print('Odds: ' + namePrice_ubet[i][1])
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
ladbrokesFileLocation = configList[21]
tabFileLocation = configList[25]
ubetFileLocation = configList[29]

# make updates to betfair file location (so as not to overwrite that created from other subprocess)
betfairFileLocation = betfairFileLocation.split('_')
newBetfairFileLocation = betfairFileLocation[0] + '_' + betfairFileLocation[1] + ' 2' + '_' + betfairFileLocation[2]

# create liquidity file
betfairLiquidityFileLocation = betfairFileLocation[0] + '_' + betfairFileLocation[1] + ' 2 Liquidity' + '_' + betfairFileLocation[2]

betfairFile = open(newBetfairFileLocation, 'w')
betfairLiquidityFile = open(betfairLiquidityFileLocation, 'w')
ladbrokesFile = open(ladbrokesFileLocation, 'w')
tabFile = open(tabFileLocation, 'w')
ubetFile = open(ubetFileLocation, 'w')

# URL to betfair race
urlBetfair = configList[3]

# URL to ladbrokes race
urlLadbrokes = configList[19]

# URL to TAB race
urlTAB = configList[23]

# URL to ubet race
urlUbet = configList[27]

# -------------------------------------------------------------
# get xpaths from TAB
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

# -------------------------------------------------------------
# xpaths to ubet horse names
horseName1_ubet = '//*[@id="page-container"]/racing-container/div/div/single-leg-container/div/div[2]/div/ul/li['

horseName2_ubet = ']/ubet-race-single-leg-grid/ul/li/div/div[1]/div/div/div/div[2]/ubet-racing-race-runner-information/div/div[2]/div[1]/div/span[1]'

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
# open Ladbrokes URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(urlLadbrokes)

browser.implicitly_wait(30)

# get names of horses
horseNames_ladbrokes = browser.find_elements_by_class_name('competitor-name')

# --------------------------------------------------
# open TAB URL
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window(browser.window_handles[1])
browser.get(urlTAB)

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

browser.switch_to.window(browser.window_handles[0])

# ---------------------------------------------------
# open ubet URL
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window(browser.window_handles[2])
browser.get(urlUbet)

# get xpaths to place odds
placeElement_ubet = []
getPlaceElements_ubet = browser.find_elements_by_xpath("//*[contains(@id,'Place')]")
i = 0
for elem in getPlaceElements_ubet:
	var = (elem.text).split('\n')
	if var[0].lower() == 'f place' or var[0].lower() == 'fixed place':
		placeElement_ubet.insert(i,elem)
		i = i + 1

numHorses_ubet = len(placeElement_ubet)

# find which horses are not scratched
i = 1
j = 1
horseNameList_ubet = []
while i <= numHorses_ubet:
	try:
		horseName_ubet = horseName1_ubet + str(j) + horseName2_ubet
		nameElement_ubet = browser.find_element_by_xpath(horseName_ubet)
		horseNameList_ubet.insert(i-1,j)
		i = i + 1
	except:
		pass
	j = j + 1

browser.switch_to.window(browser.window_handles[0])

# ---------------------------------------------------
# open betfair URL
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window(browser.window_handles[3])
browser.get(urlBetfair)

browser.switch_to.window(browser.window_handles[0])

# ---------------------------------------------------

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
	
	if handle == 0: # looking at the ladbrokes page
		print('ladbrokes')
		nameList_ladbrokes = []
		priceList_ladbrokes = []
		
		# get place odds
		# get xpaths to place odds
		paths = []
		# finds all bet options (win, place etc.)
		test = browser.find_elements_by_class_name('quickbet')

		currentTime = datetime.datetime.now()
		stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
		
		try:
			i = 0
			for elem in test:
				var = elem.get_attribute('data-bettype')
				if var == 'place':
					var2 = elem.get_attribute('data-betspecial')
					if var2 is None:
						var3 = elem.find_elements_by_xpath(".//*")
						for elem2 in var3:
							if elem2.text != "":
								ladbrokesFile.write(((horseNames_ladbrokes[i].text).replace("'","")).lower() + ',')
								ladbrokesFile.write(elem2.text + ',')
								ladbrokesFile.write(stringTime + ',')
								ladbrokesFile.write('Ladbrokes\n')
								
								nameList_ladbrokes.insert(i,((horseNames_ladbrokes[i].text).replace("'","")).lower())
								priceList_ladbrokes.insert(i,elem2.text)
							i = i + 1
		except:
			ladbrokesFile.write('Error,Error,')
			ladbrokesFile.write(stringTime + ',')
			ladbrokesFile.write('Ladbrokes\n')
			
	elif handle == 1: # looking at the TAB page
		print('TAB')
		nameList_tab = []
		priceList_tab = []
		
		currentTime = datetime.datetime.now()
		stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
		
		i = 1
		j = 0
		try:
			while i <= numHorses_tab:
				horseName_tab = horseName1_tab + str(i) + horseName2_tab
				placeName_tab = placeName1_tab + str(i) + placeName2_tab + str(columnNumber_tab) + placeName3_tab
				nameElement_tab = browser.find_element_by_xpath(horseName_tab)
				placeElement_tab = browser.find_element_by_xpath(placeName_tab).get_attribute('textContent')
				if placeElement_tab != 'SCR':
					var = (nameElement_tab.text).split('(')
					tabFile.write((((var[0]).replace("'","")).lower()).strip() + ',')
					nameList_tab.insert(j,((var[0]).replace("'","")).lower())
					tabFile.write(placeElement_tab + ',')
					priceList_tab.insert(j,placeElement_tab)
					tabFile.write(stringTime + ',')
					tabFile.write('TAB\n')
					j = j + 1
				i = i + 1
		except:
			tabFile.write('Error,Error,')
			tabFile.write(stringTime + ',')
			tabFile.write('TAB\n')
		
	elif handle == 2: # looking at ubet page
		print('Ubet')
		nameList_ubet = []
		priceList_ubet = []
		
		currentTime = datetime.datetime.now()
		stringTime = datetime.datetime.strftime(currentTime, '%b %d %Y %H:%M:%S')
		
		try:
			i = 0
			for elem in horseNameList_ubet:
				horseName_ubet = horseName1_ubet + str(elem) + horseName2_ubet
				nameElement_ubet = browser.find_element_by_xpath(horseName_ubet)
				ubetFile.write(((nameElement_ubet.text).replace("'","")).lower() + ',')
				nameList_ubet.insert(i,nameElement_ubet.text)
				var = (placeElement_ubet[i].text).split('\n')
				ubetFile.write(var[1] + ',')
				priceList_ubet.insert(i,var[1])
				ubetFile.write(stringTime + ',')
				ubetFile.write('Ubet\n')
				i = i + 1
				
		except:
			ubetFile.write('Error,Error,')
			ubetFile.write(stringTime + ',')
			ubetFile.write('Ubet\n')
	
	else: # looking at betfair site
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
			betfairFile.write('Betfair 2\n')
			betfairLiquidityFile.write(stringTime + ',')
			betfairLiquidityFile.write('Betfair Liquidity 2\n')
		
		#analyzePrices(nameList_betfair, priceList_betfair, nameList_ladbrokes, priceList_ladbrokes, nameList_tab, priceList_tab, nameList_ubet, priceList_ubet)
	
# close file handle	
ladbrokesFile.close()
tabFile.close()
ubetFile.close()
betfairFile.close()
betfairLiquidityFile.close()