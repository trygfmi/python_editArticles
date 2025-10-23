# メソッドのみなのでimportして使用してください


import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from work_directory.feature.read_env import *


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


def open_edit_articles(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
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
        
        
def click_code_editor(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
            
        driver.execute_script("arguments[0].click();", press_something_block_elements[1])
        
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
        
def print_elements(driver, search_string):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
        for element in press_something_block_elements:
            print(element)
        
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
        
def get_element_by_id(driver, search_string):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, search_string)))):
        print("要素が見つかりました")
        element=driver.find_element(By.ID, search_string)
        # print(element)
        
        return element
        
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
def getDriver():
    chrome_options = Options()
    # ユーザーデータディレクトリとプロファイルを指定
    chrome_options.add_argument("--user-data-dir="+user_data_dir)
    chrome_options.add_argument("--profile="+profile)

    # 初めてseleniumからchromeを起動してログインする時に使用
    # ボット検知を回避するための追加オプション
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # WebDriverの自動化フラグを無効化
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 自動化の通知を非表示

    return webdriver.Chrome(options=chrome_options)

def confirm_save(driver, window_handles):
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])
        title = driver.title
        print(title)
        
        print("保存する場合はokを入力してenterを押してください。しない場合はenterを押すだけで大丈夫です")
        key=input()
        if(key == "ok"):
            print("保存しました")
            press_something_block(driver, '[class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]')

        else:
            print("保存されませんでした")
            
