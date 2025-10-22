# python work_directory/start/open_all_articles.py
# input:追加したい文字列、追加したい位置を指定するための検索文字列
# output:元の文字列と追加した文字列を合わせた文字列


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from work_directory.feature.use_selenium_feature import press_something_block, open_edit_articles
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        
        print("保存する場合はokを入力してenterを押してください。しない場合はenterを押すだけで大丈夫です")
        key=input()
        if(key == "ok"):
            print("保存しました")
            press_something_block(driver, '[class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]')

        else:
            print("保存されませんでした")


start_time=time.time()
sleep_time_number=3


driver = getDriver()

# 手動でログイン用
# time.sleep(120)

driver.get(access_url)
title = driver.title
print(title)


# 編集したい記事をそのウィンドウで開く
open_edit_articles(driver, search_edit)
window_handles = driver.window_handles

    
confirm_save(driver, window_handles)


end_time=time.time()

print("かかった時間:"+str(end_time-start_time))


