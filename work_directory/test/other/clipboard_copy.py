# python work_directory/test/other/clipboard_copy.py


import pyperclip

# 配列（リスト）の例
array = ['りんご', 'バナナ', 'オレンジ']

# 配列を文字列に変換（例: 改行区切り）
text = '\n'.join(array)

# クリップボードにコピー
pyperclip.copy(text)

