# メソッドのみなのでimportして使用してください


import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sleep_time_number=0.4

def is_something_button(driver, search_string):
    return len(driver.find_elements(By.CSS_SELECTOR, search_string)) > 0
    
def press_something_block(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
        element_number=len(press_something_block_elements)-1
        # press_something_block_elements[element_number].click()
        driver.execute_script("arguments[0].click();", press_something_block_elements[element_number])
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
        
def press_something_block_print(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
        element_number=len(press_something_block_elements)
        for i in range(element_number):
            print(press_something_block_elements[i])
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
        
# ActionChainsは動作が不安定なので使用中止
# def press_something_block_actions(driver, search_string):
#     actions = ActionChains(driver)
#     # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
#     if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
#         print("要素が見つかりました")
#         press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
        
#         for element in press_something_block_elements:
#             actions.key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
            
#     else:
#         print("要素が見つかりませんでした")
#         exit(1)


def open_edit_articles(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)

        for element in press_something_block_elements:
            child_element = element.find_element(By.CSS_SELECTOR, "a")  # 子要素のdiv（class="child-class"）
            driver.execute_script("""
                var element = arguments[0];
                var event = new MouseEvent('click', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                    metaKey: true  // Commandキー（Mac）またはCtrlキー（Windows）を押した状態
                });
                element.dispatchEvent(event);
            """, child_element)
            
            time.sleep(1)
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
        
        