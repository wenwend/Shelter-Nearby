'''
Created on Jan 7, 2018

@author: wenwen
'''
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()
driver.get('https://www.google.com/maps')
#assert 'Result' in driver.title
elem = driver.find_element_by_id("searchboxinput")
elem.send_keys('shelter near me')
result=driver.find_element_by_id("searchbox-searchbutton")
result.click();

wait = WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'section-result')))

links=driver.find_elements_by_class_name('section-result-title')
for link in links:
    print link
