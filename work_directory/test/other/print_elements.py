# python work_directory/test/other/print_elements.py


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from work_directory.feature.use_selenium_feature import print_elements
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


test_access_url="https://ss523971.stars.ne.jp/todo/wp-admin/post.php?post=3475&action=edit"
test_search_string='[class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]'

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


# driver.get(access_url)
driver.get(test_access_url)
title = driver.title
print(title)


print_elements(driver, test_search_string)
time.sleep(3)


end_time=time.time()
print("かかった時間:"+str(end_time-start_time))
