# python work_directory/start/add_article_string/20251022/change_codeBackgroundColor.py
# input:追加したい文字列、追加したい位置を指定するための検索文字列
# output:元の文字列と追加した文字列を合わせた文字列


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..","..")))
from work_directory.feature.use_selenium_feature import press_something_block, is_something_button, press_something_block_print, open_edit_articles, click_code_editor, print_elements, get_element_by_id#, press_something_block_actions
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import re
import pyperclip


def addNewString(list, addList, newLengthNumber, insertNumber):
    for i in range(newLengthNumber):
        list.insert(insertNumber+i, addList[i])

def start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, elementNumber):
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])

        press_something_block(driver, '[aria-label="オプション"]')
        click_code_editor(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
        
        # 本文の要素を取得
        input_element = get_element_by_id(driver, "post-content-0")
        split_lines=input_element.get_attribute("value").splitlines()
        insertRowNumber=0
        countElementNumber=0
        for i, line in enumerate(split_lines, 0):
            if re.search(pattern, line, re.IGNORECASE):
                insertRowNumber=i
                countElementNumber+=1
                if(countElementNumber == elementNumber):
                    break
                
        
        # 本文の操作をする        
        ##################################################################
        
        addList=addString.split("\n")
        split_lines.insert(insertRowNumber+patternRowNumber, "")
        addNewString(split_lines, addList, len(addList), insertRowNumber+patternRowNumber)
        
        ##################################################################

        pyperclip.copy("\n".join(split_lines))
        driver.execute_script("arguments[0].select();", input_element)
        changed_text=pyperclip.paste()
        driver.execute_script("arguments[0].value = arguments[1];", input_element, changed_text)
        driver.execute_script("arguments[0].click();", input_element)
        input_element.send_keys("\n")
            
def confirm_save(driver, window_handles):
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])
        
        print("保存する場合はokを入力してenterを押してください。しない場合はenterを押すだけで大丈夫です")
        key=input()
        if(key == "ok"):
            print("保存しました")
            press_something_block(driver, '[class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]')

        else:
            print("保存されませんでした")

def execute_save(driver, window_handles):
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])

        print("保存しました")
        press_something_block(driver, '[class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]')
            
def replaceString(driver, window_handles, addString, pattern):
    print("hello")
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])

        press_something_block(driver, '[aria-label="オプション"]')
        click_code_editor(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
        
        # 本文の要素を取得
        input_element = get_element_by_id(driver, "post-content-0")
        split_lines=input_element.get_attribute("value").splitlines()
        insertRowNumber=0
        countElementNumber=0
        for i, line in enumerate(split_lines, 0):
            if re.search(pattern, line, re.IGNORECASE):
                insertRowNumber=i
                countElementNumber+=1
                
                # 本文の操作をする        
                ##################################################################
                
                selectedElementText=split_lines[insertRowNumber]
                resultText=selectedElementText.replace(pattern, addString)
                split_lines[insertRowNumber]=resultText
                
                ##################################################################
        

        pyperclip.copy("\n".join(split_lines))
        driver.execute_script("arguments[0].select();", input_element)
        changed_text=pyperclip.paste()
        driver.execute_script("arguments[0].value = arguments[1];", input_element, changed_text)
        driver.execute_script("arguments[0].click();", input_element)
        input_element.send_keys("\n")


start_time=time.time()
sleep_time_number=1

    
chrome_options = Options()
# ユーザーデータディレクトリとプロファイルを指定
chrome_options.add_argument("--user-data-dir="+user_data_dir)
chrome_options.add_argument("--profile="+profile)

# 初めてseleniumからchromeを起動してログインする時に使用
# ボット検知を回避するための追加オプション
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # WebDriverの自動化フラグを無効化
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 自動化の通知を非表示

driver = webdriver.Chrome(options=chrome_options)

# 手動でログイン用
# time.sleep(120)

driver.get(access_url)
title = driver.title
print(title)


# 編集したい記事をそのウィンドウで開く
open_edit_articles(driver, search_edit)
time.sleep(sleep_time_number)
window_handles = driver.window_handles


pattern = r"""#abb8c3"""
addString="#ffeeee"
replaceString(driver, window_handles, addString, pattern)


confirm_save(driver, window_handles)

# execute_save(driver, window_handles)


end_time=time.time()

print("かかった時間:"+str(end_time-start_time))





