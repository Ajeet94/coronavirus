conda environment - corona_env 
python version v3.7.7

Package Installations
conda install pandas
conda install requests
conda install beautifulsoup4
conda install matplotlib

What things do
- coronavirus_tracker_hourly.py - goes on https://www.worldometers.info/coronavirus/ and scrapes latest data from a list of countries and adds this extra entry to hourly cases.csv
- coronavirus_tracker_hourly.bat - runs coronavirus_tracker_hourly.py 
    - My windows task scheduler is set to run every hour so I get hourly updates of data

TO DO:
- Change .bat file to take current_path + filename so other users can use it from github
- Scrape worldometer for case numbers worldwide and by country (daily) dating back to January
    - implement a daily task scheduler for this
- Modify hourly code to scrape ALL countries
- Create code to compare hourly and daily numbers and see what time daily numbers are taken
- Look into what stastistical analysis to do
- Tidy and comment on code