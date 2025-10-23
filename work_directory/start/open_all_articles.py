# python work_directory/start/open_all_articles.py
# input:追加したい文字列、追加したい位置を指定するための検索文字列
# output:元の文字列と追加した文字列を合わせた文字列


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from work_directory.feature.use_selenium_feature import getDriver, confirm_save, open_edit_articles
from work_directory.feature.read_env import *


start_time=time.time()

driver = getDriver()
driver.get(access_url)
title = driver.title
print(title)

# 手動でログイン用
print("処理を継続して良い場合はokと入力してください。それ以外は処理を終了します")
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
    
confirm_save(driver, window_handles)

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


