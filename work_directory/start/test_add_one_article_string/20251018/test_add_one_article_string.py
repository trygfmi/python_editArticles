# python work_directory/start/test_add_one_article_string/20251018/test_add_one_article_string.py
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_edit)))):
    print("要素が見つかりました")
    press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_edit)

    
    child_element = press_something_block_elements[0].find_element(By.CSS_SELECTOR, "a")  # 子要素のdiv（class="child-class"）
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

else:
    print("要素が見つかりませんでした")
    exit(1)
    
    
window_handles = driver.window_handles


pattern = r"""<h3 class="wp-block-heading">windows</h3>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">WSL2</h4>
<!-- /wp:heading -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<h4 class="wp-block-heading">WSL2</h4>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">MSYS2 MINGW64</h4>
<!-- /wp:heading -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<h4 class="wp-block-heading">WSL2</h4>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:code {"backgroundColor":"cyan-bluish-gray","textColor":"#24292eff","fontSize":"1.125rem"} -->
<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/
cd</code></pre>
<!-- /wp:code -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<h4 class="wp-block-heading">MSYS2 MINGW64</h4>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:code {"backgroundColor":"cyan-bluish-gray","textColor":"#24292eff","fontSize":"1.125rem"} -->
<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/
cd</code></pre>
<!-- /wp:code -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<p>以下のコマンドをMSYS2 MINGW64に打ち込んでcommand not foundが出なければokです</p>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:paragraph -->
<p>以下のコマンドをプロンプトに打ち込んでcommand not foundが出なければokです</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">WSL2</h5>
<!-- /wp:heading -->

<!-- wp:code {"backgroundColor":"cyan-bluish-gray","textColor":"#24292eff","fontSize":"1.125rem"} -->
<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git --version</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">MSYS2 MINGW64</h5>
<!-- /wp:heading -->

<!-- wp:code {"backgroundColor":"cyan-bluish-gray","textColor":"#24292eff","fontSize":"1.125rem"} -->
<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git --version</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>※windowsはWSL2とMSYS2 MINGW64で確認しています。可能な限りWSL2をインストールしていただいて、もし設定できなかった場合はMSYS2をインストールすることで実行できますが、所々WSL2でしか実行できないコマンドが出てくるかもしれません。WSL2とMSYS2のインストール方法は下記の記事を参考にしてください</p>
<!-- /wp:paragraph -->

<!-- wp:embed {"url":"https://ss523971.stars.ne.jp/todo/2025/10/11/how-to-install-wsl2/","type":"wp-embed","providerNameSlug":"todo"} -->
<figure class="wp-block-embed is-type-wp-embed is-provider-todo wp-block-embed-todo"><div class="wp-block-embed__wrapper">
https://ss523971.stars.ne.jp/todo/2025/10/11/how-to-install-wsl2/
</div></figure>
<!-- /wp:embed -->

<!-- wp:embed {"url":"https://ss523971.stars.ne.jp/todo/2025/10/02/how-to-install-msys2/","type":"wp-embed","providerNameSlug":"todo"} -->
<figure class="wp-block-embed is-type-wp-embed is-provider-todo wp-block-embed-todo"><div class="wp-block-embed__wrapper">
https://ss523971.stars.ne.jp/todo/2025/10/02/how-to-install-msys2/
</div></figure>
<!-- /wp:embed -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<p>command not foundが出たコマンドを以下のコマンドでインストールしてください</p>"""
patternRowNumber=3
selectedElementNumber=2
addString="""<!-- wp:paragraph -->
<p>プロンプトでcommand not foundが出たコマンドを以下のコマンドでインストールしてください</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">WSL2</h5>
<!-- /wp:heading -->

<!-- wp:code {"backgroundColor":"cyan-bluish-gray","textColor":"#24292eff","fontSize":"1.125rem"} -->
<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>sudo apt install git</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">MSYS2 MINGW64</h5>
<!-- /wp:heading -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<h3 class="wp-block-heading">macos</h3>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">MacPorts</h4>
<!-- /wp:heading -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<p>command not foundが出たコマンドを以下のコマンドでインストールしてください</p>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:paragraph -->
<p>端末でcommand not foundが出たコマンドを以下のコマンドでインストールしてください</p>
<!-- /wp:paragraph -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

pattern = r"""<p>command not foundが出たコマンドを以下のコマンドでインストールしてエイリアスを設定してください</p>"""
patternRowNumber=3
selectedElementNumber=1
addString="""<!-- wp:paragraph -->
<p>ターミナルでcommand not foundが出たコマンドを以下のコマンドでインストールしてエイリアスを設定してください</p>
<!-- /wp:paragraph -->"""
start_addArticleString(driver, window_handles, addString, pattern, patternRowNumber, selectedElementNumber)

# 以下のコマンドを実行することで詳細のような文字列が出力されるはずです

# 以下のコマンドを実行することで詳細のような文字列が出力されるはずです
    
confirm_save(driver, window_handles)


end_time=time.time()

print("かかった時間:"+str(end_time-start_time))


