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
  * Ability to open multiple tabs using the same webdriver instance.
