# python work_directory/start/add_article_string/20251028/addDetail.py
# input:追加したい文字列、追加したい位置を指定するための検索文字列
# output:元の文字列と追加した文字列を合わせた文字列


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..","..")))
from work_directory.feature.use_selenium_feature import press_something_block, open_edit_articles, click_code_editor, get_element_by_id
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
                
def changeElementAttribute(driver, window_handles, addString1, addString2, deletePattern1, deletePattern2):
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
            if re.search(deletePattern1, line, re.IGNORECASE):
                insertRowNumber=i
                countElementNumber+=1
                
                # 本文の操作をする        
                ##################################################################
                
                selectedElementText=split_lines[insertRowNumber]
                resultText1=selectedElementText.replace(deletePattern1, "")
                # print(resultText1)
                resultText2=resultText1.replace(deletePattern2, "")
                # print(resultText2)
                
                resultString=addString1+resultText2+addString2
                print(resultString)
                split_lines[insertRowNumber]=resultString
                
                ##################################################################
                        
                pyperclip.copy("\n".join(split_lines))
                driver.execute_script("arguments[0].select();", input_element)
                changed_text=pyperclip.paste()
                driver.execute_script("arguments[0].value = arguments[1];", input_element, changed_text)
                driver.execute_script("arguments[0].click();", input_element)
                input_element.send_keys("\n")
                
def getElementValue(driver, window_handles, deletePattern1, deletePattern2, elementNumber):
    valueArray=[]
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
            if re.search(deletePattern1, line, re.IGNORECASE):
                insertRowNumber=i
                countElementNumber+=1
                
                if(countElementNumber == elementNumber):
                    # 本文の操作をする        
                    ##################################################################
                    
                    selectedElementText=split_lines[insertRowNumber]
                    resultText1=selectedElementText.replace(deletePattern1, "")
                    # print(resultText1)
                    resultText2=resultText1.replace(deletePattern2, "")
                    # print(resultText2)
                    
                    valueArray.append(resultText2)
                    
                    break
                
            elif(i == len(split_lines)-1):
                valueArray.append("")
    
                
    return valueArray

def start_addArticleStringArray(driver, window_handles, addStringArray, pattern, patternRowNumber, elementNumber):
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
        for j, line in enumerate(split_lines, 0):
            if re.search(pattern, line, re.IGNORECASE):
                insertRowNumber=j
                countElementNumber+=1
                if(countElementNumber == elementNumber):
                    break
                
        
        # 本文の操作をする        
        ##################################################################
        
        print("insertRowNumber:"+str(insertRowNumber))
        print("i:"+str(i))
        addList=addStringArray[i-1]
        split_lines.insert(insertRowNumber+patternRowNumber, "")
        addNewStringLine(split_lines, addList, insertRowNumber+patternRowNumber)
        
        ##################################################################

        pyperclip.copy("\n".join(split_lines))
        driver.execute_script("arguments[0].select();", input_element)
        changed_text=pyperclip.paste()
        driver.execute_script("arguments[0].value = arguments[1];", input_element, changed_text)
        driver.execute_script("arguments[0].click();", input_element)
        input_element.send_keys("\n")
        
def addNewStringLine(list, addList, insertNumber):
    list.insert(insertNumber, addList)


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
time.sleep(sleep_time_number)
window_handles = driver.window_handles


deletePattern1 = r"""<pre class="wp-block-code has-24292-eff-color has-text-color has-background has-1-125-rem-font-size" style="background-color:#ffeeee"><code>"""
deletePattern2 = r"""</code></pre>"""
addString1="""<!-- wp:details -->
<details class="wp-block-details"><summary>詳細</summary><!-- wp:paragraph -->
<pre class="wp-block-code has-24292-eff-color has-text-color has-background has-1-125-rem-font-size" style="background-color:#ffeeee"><code>"""
addString2="""</code></pre>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->"""
elementNumber=3
valueArray=getElementValue(driver, window_handles, deletePattern1, deletePattern2, elementNumber)
print(valueArray)


for i, line in enumerate(valueArray, 0):
    addStringCat = addString1+line
    addStringCat = addStringCat+addString2
    valueArray[i] = addStringCat
    
pattern="""<h5 class="wp-block-heading">MSYS2 MINGW64</h5>"""
patternRowNumber=-1
elementNumber=3
start_addArticleStringArray(driver, window_handles, valueArray, pattern, patternRowNumber, elementNumber)



confirm_save(driver, window_handles)

# execute_save(driver, window_handles)


end_time=time.time()

print("かかった時間:"+str(end_time-start_time))





