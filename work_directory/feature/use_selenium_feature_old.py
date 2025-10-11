# メソッドのみなのでimportして使用してください


import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


sleep_time_number=0.4

def hello():
    print("hello add_block")
    
def press_something_block(driver, search_string):
    press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
    element_number=len(press_something_block_elements)-1
    ActionChains(driver)\
        .click(press_something_block_elements[element_number])\
        .perform()
        
    time.sleep(sleep_time_number)
        
def press_something_iframe_block(driver, search_string):
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe)
    
    press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
    ActionChains(driver)\
        .click(press_something_block_elements[0])\
        .perform()
        
    driver.switch_to.default_content()
        
def add_something_block(driver, search_string):
    something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
    ActionChains(driver)\
        .click(something_block_elements[0])\
        .perform()
        
    time.sleep(sleep_time_number)
        
def add_something_data(driver, search_string, insert_string):
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe)
    
    add_something_data_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
    
    pyperclip.copy(insert_string)
    element_number=len(add_something_data_elements)-1
    ActionChains(driver)\
        .click(add_something_data_elements[element_number])\
        .key_down(Keys.COMMAND)\
        .send_keys("v")\
        .key_up(Keys.COMMAND)\
        .perform()
    
    driver.switch_to.default_content()

