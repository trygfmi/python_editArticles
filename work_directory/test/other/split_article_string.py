# python work_directory/test/other/split_article_string.py


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from work_directory.feature.use_selenium_feature import press_something_block, is_something_button, press_something_block_print, open_edit_articles, click_code_editor, print_elements, get_element_by_id#, press_something_block_actions
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import re
import pyperclip


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

# 手動でログイン用
# time.sleep(120)

driver.get(access_url)
title = driver.title
print(title)


# 編集したい記事をそのウィンドウで開く
print("original windowを取得")
original_window = driver.current_window_handle
time.sleep(sleep_time_number)
open_edit_articles(driver, search_edit)
time.sleep(sleep_time_number)
window_handles = driver.window_handles
for i in range(1,len(window_handles)):
    print(i)
    driver.switch_to.window(window_handles[i])
    # time.sleep(1)
    press_something_block(driver, '[aria-label="オプション"]')
    # time.sleep(1)
    click_code_editor(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
    
    input_element = get_element_by_id(driver, "post-content-0")
    # input_element = get_element_by_id(driver, "inspector-textarea-control-0")
    split_lines=input_element.get_attribute("value").splitlines()
    # split_lines=input_element.get_attribute("value")
    
    # pattern = r"test"
    # pattern = r"上記のコマンドをインストール済みの方は、以下のコマンドを実行してリポジトリからダウンロード後、ディレクトリを移動し、chgrpコマンドを実行してshell scriptの挙動を確認してください"
    # patternに指定する文字列は1行のみ
    # pattern = r"""<!-- wp:embed {"url":"https://ss523971.stars.ne.jp/todo/2025/10/02/macports%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e3%81%be%e3%81%a7%e3%81%ae%e6%89%8b%e9%a0%86/","type":"wp-embed","providerNameSlug":"todo"} -->"""
    pattern = r"<p>※MSYS2 MINGW64を使用しています</p>"

    deleteRowNumber=0
    matching_lines = []
    for i, line in enumerate(split_lines, 0):
        if re.search(pattern, line, re.IGNORECASE):
            deleteRowNumber=i
            
    # 3行分を削除
    del split_lines[deleteRowNumber-1:deleteRowNumber+2]
    split_lines.insert(deleteRowNumber-1, "hello world")
    for line in split_lines:
        print(line)
    # print("split_lines:"+split_lines[5]+" length:"+str(len(split_lines)))  # 例: "input" や "textarea" が出力されるべき
    
    pyperclip.copy('\n'.join(split_lines))
    # pyperclip.copy("hello"+split_lines)
    driver.execute_script("arguments[0].select();", input_element)
    
    changed_text=pyperclip.paste()
    # print(changed_text)
    driver.execute_script("arguments[0].value=arguments[1];", input_element, changed_text)
    # pyperclip.paste()
    time.sleep(5)
    
    
time.sleep(sleep_time_number)
driver.switch_to.window(original_window)
time.sleep(sleep_time_number)
exit

# すべて受け取るボタンを押す
time.sleep(sleep_time_number)
# すでに受け取っている場合何もしないようにする
if(is_something_button(driver, search_mission_receive_button)):
    press_something_block(driver, search_mission_receive_button)

    #すべて受け取るボタンをを押した後のokボタンを押す処理を追加する必要あり
    time.sleep(sleep_time_number)
    press_something_block(driver, search_mission_receive_ok_button)

time.sleep(sleep_time_number)

end_time=time.time()

print("かかった時間:"+str(end_time-start_time))
