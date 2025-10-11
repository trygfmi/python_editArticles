# python work_directory/start/start_editArticles.py


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from work_directory.feature.use_selenium_feature import press_something_block, is_something_button, press_something_block_print, open_edit_articles#, press_something_block_actions
from work_directory.feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

# time.sleep(180)

# ログアウトしている時を考慮して、今後ログインする処理を追加する必要がある

# time.sleep(sleep_time_number)
# # すでに受け取っている場合何もしないようにする
# if(is_something_button(driver, search_point_present_box)):
#     press_something_block(driver, search_point_present_box)

#     #プレゼントボックスを押した後のokボタンを押す処理を追加する必要あり
#     time.sleep(sleep_time_number)
#     press_something_block(driver, search_point_present_box_ok_button)

# 編集したい記事をそのウィンドウで開く
print("original windowを取得")
original_window = driver.current_window_handle
time.sleep(sleep_time_number)
# press_something_block_print(driver, search_edit)
# press_something_block(driver, search_edit)
# press_something_block_actions(driver, search_edit)
open_edit_articles(driver, search_edit)
time.sleep(sleep_time_number)
window_handles = driver.window_handles
for handle in window_handles:
    time.sleep(1)
    driver.switch_to.window(handle)
    
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
