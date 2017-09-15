import os
import subprocess
import datetime
import time

# *** PROCESS: ***
# read first set of parameters
# print to configuration file
# two hours before race start launch subprocess
# read next set of parameters
# repeat

# filepath to directory containing this file
curPath = 'C:/Users/Charith/Python Files'
originalDir = os.path.dirname(curPath)

# filepath to directory containing file running subprocess (i.e scanning betting sites)
targetPath = 'C:/Users/Charith/Python Files'

# filepath to directory containing data files
dataPath = 'C:/Users/Charith/Desktop/Data Files'

raceListFileLocation = 'C:/Users/Charith/Desktop/Race List.txt'
configFileLocation = 'C:/Users/Charith/Desktop/Configuration File.txt'

# read parameters from race list file
with open(raceListFileLocation) as f:
    raceList = f.read().splitlines(1)
	
# get total number of races
numRaces = int((len(raceList) - 1) / 8)

i = 0
while i < numRaces:
	# read parameters
	startTime = raceList[((10 * i) + 1)]
	raceName = raceList[((10 * i) + 3)]
	betfairURL = raceList[((10 * i) + 5)]
	williamHillURL = raceList[((10 * i) + 7)]
	centrebetURL = raceList[((10 * i) + 9)]
	print(startTime)
	# print to configuration file
	with open(configFileLocation, 'r') as configFile:
		# read a list of lines into data
		data = configFile.readlines()

	# change config file contents
	raceName = raceName.splitlines()
	betfairFileName = dataPath + '/' + str((startTime.replace(":","")).rstrip('\n')) + '_Betfair_' + str(raceName[0]) + '.csv\n'
	williamHillFileName = dataPath + '/'  + str((startTime.replace(":","")).rstrip('\n')) + '_William Hill_' + str(raceName[0]) + '.csv\n'
	centrebetFileName = dataPath + '/' + str((startTime.replace(":","")).rstrip('\n')) + '_Centrebet_' + str(raceName[0]) + '.csv\n'
	
	data[1] = startTime
	data[3] = betfairURL
	data[5] = betfairFileName
	data[7] = williamHillURL
	data[9] = williamHillFileName
	data[11] = centrebetURL
	data[13] = centrebetFileName
    
	# write everything back
	with open(configFileLocation, 'w') as configFile:
		configFile.writelines(data)
		
	startTimeString = data[1].splitlines()
	raceStartTime = datetime.datetime.strptime(startTimeString[0], '%b %d %Y %H:%M')
	
	# get current time
	currentTime = datetime.datetime.now()

	while currentTime < (raceStartTime - datetime.timedelta(minutes=130)):
		time.sleep(60)
		
	# launch subprocess
	print('launching subprocess ' + str(i + 1))
	os.chdir(targetPath)
	subprocess.Popen("python v2.0.0.py", shell=True)
	os.chdir(originalDir)
	
	time.sleep(100)
	
	i = i + 1
	

	
