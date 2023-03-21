import requests
import scrapy
from scrapy import Spider
import logging
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

season = ["2017-18", "2018-19"]

url = "https://www.nba.com/stats/cumestats?TeamID=1610612737&Season=2017-18"


driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install())) 

driver.get(url)
try:
    time.sleep(5)
    element_cookie=driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    element_cookie.click()
except:
    logging.info('No cookie') 

try:
    time.sleep(5)
    element_terms_of_use=driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/button')
    element_terms_of_use.click()
except:
    logging.info('No terms of use') 
try:
    time.sleep(5)
    element_select_all=driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section/div/div/div/div/div[4]/div/div[1]/button[2]')
    element_select_all.click()
except:
    logging.info('Element select all failed') 

try:
    time.sleep(5)
    element_move_selected=driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section/div/div/div/div/div[4]/div/div[1]/button[1]')
    element_move_selected.click()
except:
    logging.info('Element move all failed') 

try:
    time.sleep(5)
    element_run=driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section/div/div/div/div/div[4]/div/div[2]/div/button[3]')
    element_run.click()
except:
    logging.info('Element run failed') 


try:
    time.sleep(5)
    element_run=driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section/div/div/div/div[2]/button[1]')
    element_run.click()
    time.sleep(10)
except:
    logging.info('Download failed') 
