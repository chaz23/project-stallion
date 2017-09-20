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

# URL to crownbet race of interest
url = 'https://crownbet.com.au/racing-betting/horse-racing/geelong/20170917/race-5-705365-23775107'

# open that URL
browser.execute_script("window.open('about:blank', 'tab1');")
browser.switch_to.window(browser.window_handles[0])
browser.get(url)

browser.implicitly_wait(10)

# var2 = browser.find_element_by_css_selector('#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div.column.tote-header.tote-x2 > table > tbody > tr:nth-child(2) > td.tote-subheader.col2.x2').get_attribute('textContent')
# print(var2)

var = browser.find_elements_by_class_name('')





# css selectors to fixed, best tote etc.
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div.column.tote-header.tote-x2 > table > tbody > tr:nth-child(1) > td
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div:nth-child(3) > table > tbody > tr:nth-child(1) > td
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div:nth-child(4) > table > tbody > tr:nth-child(1) > td



# css selectors to win, place etc.
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div.column.tote-header.tote-x2 > table > tbody > tr:nth-child(2) > td.tote-subheader.col1.x2
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div.column.tote-header.tote-x2 > table > tbody > tr:nth-child(2) > td.tote-subheader.col2.x2
#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div:nth-child(3) > table > tbody > tr:nth-child(2) > td

#events > div:nth-child(1) > div > div.event-wrapper > div.middle-section.outcomes-header.clearfix > div > div.win-place.hidden-xs > div > table > tbody > tr:nth-child(2) > td.tote-subheader.col2.x2


# css selectors to place odds








# # xpaths to fixed, best tote etc.
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[1]/td
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[3]/table/tbody/tr[1]/td
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[4]/table/tbody/tr[1]/td

# # xpaths to win, place etc.
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[2]/td[1]
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[2]/td[2]
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[3]/table/tbody/tr[2]/td
# //*[@id="events"]/div[1]/div/div[2]/div[4]/div/div[3]/div[4]/table/tbody/tr[2]/td

# # xpaths to place odds
# //*[@id="events"]/div[1]/div/div[2]/div[8]/table/tbody/tr[1]/td[5]/a/span
# //*[@id="events"]/div[1]/div/div[2]/div[8]/table/tbody/tr[3]/td[5]/a/span






















