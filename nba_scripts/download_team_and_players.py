from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import os

report_type = ["Team", "Player"]

for i in report_type:
 
    url = f'https://www.nba.com/stats/cumestats?LeagueID=00&ReportType={i}' 
    
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install())) 
    
    driver.get(url) 

    working_dir=os.getcwd()
    filename = f'{working_dir}/nba_com_{i}.html'
    with open(filename, 'w') as f:
        f.write(driver.page_source)
 