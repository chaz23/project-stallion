# Documentation for Project Stallion Version Control

## Version 1.0.0
Download data from individual races from Betfair and William Hill.
Capture data every second and store as CSV files with columns:

  **Betfair**
  1. Horse name
  2. Back multiplier
  3. Lay multiplier
  
  **William Hill**
  1. Horse name
  2. Win multiplier
  3. Place multiplier
  
  * Race page URLs must be manually input into the source code.
  * Race start times must be manually input into the source code.
  * Only one race can be analyzed at a time.
  
## Version 1.1.0
  * Included headless browsing capabilities using PhantomJS.
  * Ability to open two tabs using the same webdriver instance.
  
Toggle between Betfair and William Hill sites. Extract data and print to file.

## Version 1.2.0
  * Ability to open multiple tabs using the same webdriver instance.
  * Added data extraction from Centrebet.
  * Time resolution ~5 seconds.

## Version 1.3.0
  * Added data extraction from Unibet.
  * Unibet extraction making program extremely slow.

## Version 1.4.0
  * Removed Unibet data extraction - only Betfair, William Hill and Centrebet.
  * Time resolution ~1 second.
  * All parameters are now read from configuration file.
  * Updated data extraction methods from all 3 sites.

## Version 1.6.0
  * Added functionality to analyze multiple races by launching each race as a subprocess.
  * Race details mut be entered in advance into file 'Race List.txt'.

## Version 1.7.0
  * Bug fixes in place odds analysis function.
  * Improved stability when reading William Hill pages.
