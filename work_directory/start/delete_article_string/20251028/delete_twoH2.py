# python work_directory/start/delete_article_string/20251028/delete_twoH2.py
# input:追加したい文字列、追加したい位置を指定するための検索文字列
# output:元の文字列と追加した文字列を合わせた文字列


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))
from work_directory.feature.use_selenium_feature import press_something_block, open_edit_articles, click_code_editor, get_element_by_id
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import re
import pyperclip

    
def deleteListElement(list, deleteNumber, beforeNumber, afterNumber):
    del list[deleteNumber-beforeNumber:deleteNumber+afterNumber]
    
def start_deleteArticleString(driver, window_handles, pattern, beforeNumber, afterNumber, elementNumber):
    for i in range(1,len(window_handles)):
        print(i)
        driver.switch_to.window(window_handles[i])

        press_something_block(driver, '[aria-label="オプション"]')
        click_code_editor(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
        
        # 本文の要素を取得
        input_element = get_element_by_id(driver, "post-content-0")
        split_lines=input_element.get_attribute("value").splitlines()
        deleteRowNumber=0
        countElementNumber=0
        for i, line in enumerate(split_lines, 0):
            if re.search(pattern, line, re.IGNORECASE):
                deleteRowNumber=i
                countElementNumber+=1
                if(countElementNumber == elementNumber):
                    break
                
        # 本文の操作をする        
        ##################################################################

        # 3行分と空行を削除
        deleteListElement(split_lines, deleteRowNumber, beforeNumber, afterNumber)
        
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
   

start_time=time.time()
sleep_time_number=3


chrome_options = Options()
# ユーザーデータディレクトリとプロファイルを指定
chrome_options.add_argument("--user-data-dir="+user_data_dir)
chrome_options.add_argument("--profile="+profile)

# 初めてseleniumからchromeを起動してログインする時に使用
# ボット検知を回避するための追加オプション
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # WebDriverの自動化フラグを無効化
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 自動化の通知を非表示

driver = webdriver.Chrome(options=chrome_options)

driver.get(access_url)
title = driver.title
print(title)



print("処理を続行する場合はokを入力してください、しない場合はenterを押すだけで処理を終了します")
continueString=input()
if(continueString == "ok"):
    print("処理を続行します")
else:
    print("処理を終了します")
    driver.quit()
    exit(1)



# 編集したい記事をそのウィンドウで開く
open_edit_articles(driver, search_edit)
window_handles = driver.window_handles


# <h2 class="wp-block-heading">この記事で使用したコマンドで実行できるお薦め記事</h2>
pattern = r"""<h2 class="wp-block-heading">この記事で使用したコマンドで実行できるお薦め記事</h2>"""
beforeNumber=1
afterNumber=3
selectedElementNumber=1
start_deleteArticleString(driver, window_handles, pattern, beforeNumber, afterNumber, selectedElementNumber)

# <h2 class="wp-block-heading">この記事で使用しているキーボード</h2>
pattern = r"""<h2 class="wp-block-heading">この記事で使用しているキーボード</h2>"""
beforeNumber=1
afterNumber=3
selectedElementNumber=1
start_deleteArticleString(driver, window_handles, pattern, beforeNumber, afterNumber, selectedElementNumber)

    
confirm_save(driver, window_handles)


end_time=time.time()

print("かかった時間:"+str(end_time-start_time))





